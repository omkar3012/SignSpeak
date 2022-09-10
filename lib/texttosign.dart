import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class MyCustomForm extends StatefulWidget {
  const MyCustomForm({Key? key}) : super(key: key);

  @override
  _MyCustomFormState createState() => _MyCustomFormState();
}

// Define a corresponding State class.
// This class holds the data related to the Form.
class _MyCustomFormState extends State<MyCustomForm> {
  // Create a text controller and use it to retrieve the current value
  // of the TextField.
  final myController = TextEditingController();
  String input = '_';
  List<Image> listOfImages = [];
  List<String> result = [];

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    myController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Text to Sign",
        ),
      ),
      body: Column(
        children: [
          Expanded(
            flex: 1,
            child: Card(
              child: TextField(
                controller: myController,
              ),
            ),
          ),
          Expanded(
            flex: 1,
            child: Center(
              child: TextButton(
                onPressed: () {
                  setState(() {
                    input = myController.text;
                    // for (int i = 1; i < listOfImages.length; i++) {
                    //   var char = input[i];
                    //   listOfImages.add(
                    //       Image(image: AssetImage("assets/images/$char.png")));
                    // }
                    result = input.split(" ");
                    for(int i = 0; i < result.length; i++){
                      result[i] =  "assets/images/" + result[i] + ".png";
                    }
                    // result.trimRight();
                    print(result);
                    // listOfImages.add(Image.asset("assets/images/$input.png"));
                    // result.add("assets/images/$input.png");
                  });
                },
                child: Text(
                  "Enter",
                ),
              ),
            ),
          ),
          // Expanded(
          //   flex: 3,
          //   child: Center(child: Image.asset("assets/images/$input.png")),
          // ),
          Expanded(
            child: ListView.builder(
              itemBuilder: (BuildContext, index) {
                return Container(
                  child: Image(
                    image: AssetImage(result[index]),
                  ),
                );
              },
              itemCount: result.length,
              // shrinkWrap: true,

              padding: EdgeInsets.all(5),
              scrollDirection: Axis.horizontal,
            ),
          )
        ],
      ),
    );
  }
}

//
// import 'package:flutter/cupertino.dart';
// import 'package:flutter/material.dart';
//
// void main() {
//   runApp(MyCustomForm());
// }
//
// class MyCustomForm extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//         title: 'Flutter App Learning',
//         theme: ThemeData(
//           primarySwatch: Colors.green,
//         ),
//         home: MyHomePage()
//     );
//   }
// }
//
// class MyHomePage extends StatefulWidget {
//   MyHomePage({Key? key}) : super(key: key);
//   @override
//   _MyHomePageState createState() => _MyHomePageState();
// }
//
// class _MyHomePageState extends State<MyHomePage> {
//   List<String> images = [
//     "assets/images/scenary.jpg",
//     "assets/images/scenary_red.jpg",
//     "assets/images/waterfall.jpg",
//     "assets/images/tree.jpg",
//   ];
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//         appBar: AppBar(
//           title: Text("Flutter ListView"),
//         ),
//         body: ListView.builder(
//           itemBuilder: (BuildContext, index) {
//             return Card(
//               child: ListTile(
//                 leading: CircleAvatar(
//                   backgroundImage: AssetImage(images[index]),),
//                 title: Text("This is title"),
//                 subtitle: Text("This is subtitle"),
//               ),
//             );
//           },
//           itemCount: images.length,
//           shrinkWrap: true,
//           padding: EdgeInsets.all(5),
//           scrollDirection: Axis.vertical,
//         )
//     );
//   }
// }
