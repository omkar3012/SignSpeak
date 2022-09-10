import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:tflite/tflite.dart';
import 'signtosign.dart';
import 'signtotext.dart';
import 'texttosign.dart';


void main() {
  return runApp(
    const MyApp(),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(
          backgroundColor: Colors.white,
          title: Center(
            child: const Text(
              "SignSpeak",
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Colors.black,
              ),
            ),
          ),
        ),
        body: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Padding(
              padding: const EdgeInsets.all(18.0),
              child: SizedBox(
                height: 100.0,
                width: 200.0,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                      primary: Colors.orangeAccent,
                      padding:
                      EdgeInsets.symmetric(horizontal: 50, vertical: 20),
                      textStyle:
                      TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
                  child: const Text(
                    "Sign To Text",
                    style: TextStyle(
                      color: Colors.white,
                    ),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const ImageDetectApp(),
                      ),
                    );
                  },
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(18.0),
              child: SizedBox(
                height: 100.0,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                      primary: Colors.orange,
                      padding:
                      EdgeInsets.symmetric(horizontal: 50, vertical: 20),
                      textStyle:
                      TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
                  child: const Text(
                    "Text To Sign",
                    style: TextStyle(color: Colors.white),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const MyCustomForm(),
                      ),
                    );
                  },
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(18.0),
              child: SizedBox(
                height: 100.0,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                      primary: Colors.deepOrangeAccent,
                      padding:
                      EdgeInsets.symmetric(horizontal: 50, vertical: 20),
                      textStyle:
                      TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
                  child: const Text(
                    "Sign To Sign",
                    style: TextStyle(
                      color: Colors.white,
                    ),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const SignToSign(),
                      ),
                    );
                  },
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}