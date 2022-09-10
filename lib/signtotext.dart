import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:tflite/tflite.dart';


// class SignToText extends StatefulWidget {
//   const SignToText({Key? key}) : super(key: key);
//
//   @override
//   State<SignToText> createState() => _SignToTextState();
// }

//
// class _SignToTextState extends State<SignToText> {
//   @override
//   Widget build(BuildContext context) {
//     return SafeArea(
//       child: Scaffold(
//         appBar: AppBar(
//           title: Text(
//               "Sign to Text"),
//         ),
//       ),
//     );
//   }
// }

class ImageDetectApp extends StatefulWidget {
  const ImageDetectApp({Key? key}) : super(key: key);

  @override
  State<ImageDetectApp> createState() => _ImageDetectAppState();
}

class _ImageDetectAppState extends State<ImageDetectApp> {
  var finalResult;
  var sentence = "";//Final value which stores label of image
  PickedFile? imageFile;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Sign to Text"),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              ElevatedButton(
                child: Text("Select New Image"),
                onPressed: () {
                  _imageSelection();
                },
              ),
              SizedBox(height: 50.0,),
              ElevatedButton(
                child: Text("Capture New Image"),
                onPressed: () {
                  _imageSelection2();
                },
              ),
              SizedBox(height: 50.0,),
              Card(
                color: Colors.blue,
                child: Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: Row(
                    children: [
                      Text(
                        "Output: ",
                        style: TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      SizedBox(
                        width: 10.0,
                      ),
                      Text(
                        "$sentence",
                        style: TextStyle(
                          color: Colors.white,
                          // fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              // Text("$output")
            ],
          ),
        ),
      ),
    );
  }

  List? _listResult;
  late XFile? _imageFile;
  late bool _loading = false;

  @override
  void initState() {
    super.initState();
    _loading = true;
    _loadModel();
  }

  void _loadModel() async {
    await Tflite.loadModel(
      model: "assets/model_unquant.tflite",
      labels: "assets/labels.txt",
    ).then((value) {
      setState(() {
        _loading = false;
      });
    });
  }

  void _imageSelection() async {
    var imageFile = await ImagePicker().pickImage(source: ImageSource.gallery);
    setState(() {
      _loading = true;
      _imageFile = imageFile;
    });
    _imageClasification(imageFile!);
  }

  void _imageSelection2() async {
    var imageFile = await ImagePicker().pickImage(source: ImageSource.camera);
    setState(() {
      _loading = true;
      _imageFile = imageFile;
    });
    _imageClasification(imageFile!);
  }

  void _imageClasification(XFile image) async {
    var output = await Tflite.runModelOnImage(
      path: image.path,
      numResults: 2,
      threshold: 0.5,
      imageMean: 127.5,
      imageStd: 127.5,
    );
    setState(() {
      _loading = false;
      _listResult = output;
      finalResult = _listResult?[0]['label'];
      if( finalResult != null) {
        sentence = sentence + " " + finalResult.toString();
      }
      // convert = finalResult;
      print("The list is ");
      print(finalResult);
    });
  }

  @override
  void dispose() {
    Tflite.close();
    super.dispose();
  }
}
