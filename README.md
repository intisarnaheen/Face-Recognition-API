# Face Recognition API
<p align="left"> 
<img src="https://komarev.com/ghpvc/?username=intisarnaheen&color=blueviolet" alt="watching_count" />
  <img src="https://img.shields.io/badge/Focus-Computer%20Vision%2C%20Machine%20Learning-brightgreen" />
  <img src="https://img.shields.io/badge/License-MIT-blue" />
</p>

![Results_image](https://raw.githubusercontent.com/intisarnaheen/Face-Recognition-API/main/snapshots/adf3f3a5acf468eb1a2e23849ddbe4ec.gif)

<div id="top"></div>

<br />

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project


Face recognition is a technology capable of identifying or verifying a subject through an image, video or any audiovisual element of his face. Generally, this identification is used to access an application, system or service. Our system has two segments, one is the detector and another one is recognizer. And entirely it works through the API from our system. Few biometric technologies are sparking our imagination quite like facial recognition. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Used Libraries

This project was successfully built with the following libraries. To install the libraries and use the codebase, you should properly be aware of the version conflicts of tensorflow and numpy as well. But I strongly recommend to use Anaconda for that.

* [OpenCV](https://opencv.org/)
* [numpy](https://numpy.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [Pickle](https://docs.python.org/3/library/pickle.html)
* [Glob](https://docs.python.org/3/library/glob.html)


<p align="right">(<a href="#top">back to top</a>)</p>


## How it works

Based on the system of my project, the technical procedures has these breakdowns. Face Recognition API is the process of identifying or verifying the identity of a person using their face. It captures, analyzes, and compares patterns based on the person's facial details.

* The face detection process is an essential step in detecting and locating human faces in images and realtime videos(on upcoming updates)
* The face capture process transforms analog information (a face) into a set of digital information (data or vectors) based on the person's facial features.
* The face match process verifies if two faces belong to the same person and pops up with a string of the detected person's name fetched from the database through API.



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/intisarnaheen/Face-Recognition-API.git
   ```
2. Install OpenCV
   ```sh
   pip install opencv-python
   ```
3. Install numpy
   ```sh
   pip install numpy
   ```
4. Install Tensorflow
   ```sh
   pip install tensorflow
   ```
5. Install Pickle
   ```sh
   pip install pickle5
   ```
6. Install Glob
   ```sh
   pip install glob2
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


## Usage

In the Codebase, you will find a folder named 'Checkpoint'. There are some data files and pretrained models those are loaded into the main stream. There is a python file named 'test_img.py', that is used to recognize from an image. Let's have a look where pretrained model is loaded and where the output recognized image data is saved and some stuffs:

   ```sh
   file = open(path+"/embds_dict_ad.pkl", 'rb') #Line number 21
   ```
   ```sh
   cfg = load_yaml(path+'/configs/arc_res50.yaml') #Line number 32
   ```
Here the first line does the embedding part and the second one loads the data.
   ```sh
   test_path="/home/Face-Recognition/test_images/" #Line number 96
   ```
You can run this .py file and test your sample images setting your own directory in this line.
Same like this algorithm, test_frame.py works the same; but it works for the video file instead. For example, it can work with realtime camera or video file and read that frame by frame and recognize it and save the cropped recognized face afterwards. The whole recognition process is validated through the API which is the backbone here.
The file app.py hold this API. This API holds two methods: GET & POST.
   ```sh
    @app.route('/recognition', methods=['POST']) #Line number 27
    .
    .
    .
    .
    return jsonify({'result': 'error during prediction', 'error': e}) #Line number 42
   ``` 
This function receives the request to check the image or frame from the model and sends the response in JSON format to the application.

<p align="right">(<a href="#top">back to top</a>)</p>


## Software Architecture Diagram

In this section we analyze the performance of our mellowmax policy. Here, we compare the influence of the number of memory states of the fsc. It is expected that as the number of memory states increases the performance of the finite state controller should improve.

![Results_image](https://raw.githubusercontent.com/intisarnaheen/Bayesian-Reinforcement-Learning-with-Maximum-Entropy/master/Snapshots/Number%20of%20iterations.PNG)


## Contribution

Contributions are what make the open source community such an amazing place to learn, inspire, and create. For any queries, feel free to contact me and if you are willing to collaborate with me, I will highly appreciate that. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Face-Recognition-API`)
3. Commit your Changes (`git commit -m 'Add some Face-Recognition-API'`)
4. Push to the Branch (`git push origin feature/Face-Recognition-API`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


## Contact

[@Follow me on twitter](https://twitter.com/itnsir) <br>
Email me - intisar.naheen@northsouth.edu <br>
Project Link: [Face Recognition API](https://github.com/intisarnaheen/Face-Recognition-API)

<p align="right">(<a href="#top">back to top</a>)</p>

## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [CPSD Technologies Limited](#)


<p align="right">(<a href="#top">back to top</a>)</p>



