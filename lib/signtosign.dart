import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:tflite/tflite.dart';

class SignToSign extends StatefulWidget {
  const SignToSign({Key? key}) : super(key: key);

  @override
  State<SignToSign> createState() => _SignToSignState();
}

class _SignToSignState extends State<SignToSign> {
  var finalResult;
  String stringResult = '_'; //Final value which stores label of image
  PickedFile? imageFile;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Sign to Sign"),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              ElevatedButton(
                child: Text("Capture New Image"),
                onPressed: () {
                  _imageSelection();
                },
              ),
              SizedBox(
                height: 50.0,
              ),
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
                        "$finalResult",
                        style: TextStyle(
                          color: Colors.white,
                          // fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              SizedBox(
                height: 50.0,
              ),
              Center(
                child: Image(
                  image: AssetImage(
                    "assets/images/$stringResult.png",
                  ),
                ),
              ), // Text("$output")
            ],
          ),
        ),
      ),
    );
  }

  List? _listResult;
  late PickedFile? _imageFile;
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
    var imageFile = await ImagePicker().getImage(source: ImageSource.camera);
    setState(() {
      _loading = true;
      _imageFile = imageFile;
    });
    _imageClasification(imageFile!);
  }

  void _imageClasification(PickedFile image) async {
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
      finalResult = _listResult?[0]['label'][2];
      // convert = finalResult;
      stringResult = finalResult.toString();
      print(finalResult);
    });
  }

  @override
  void dispose() {
    Tflite.close();
    super.dispose();
  }
}
