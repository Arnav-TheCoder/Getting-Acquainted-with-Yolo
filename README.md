# Getting-Acquainted-with-Yolo
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->

![Contributors](https://img.shields.io/github/contributors/Arnav-TheCoder/Getting-Acquainted-with-Yolo.svg?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/Arnav-TheCoder/Getting-Acquainted-with-Yolo.svg?style=for-the-badge)
![Stargazers](https://img.shields.io/github/stars/Arnav-TheCoder/Getting-Acquainted-with-Yolo.svg?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/Arnav-TheCoder/Getting-Acquainted-with-Yolo.svg?style=for-the-badge)
![project_license](https://img.shields.io/github/license/Arnav-TheCoder/Getting-Acquainted-with-Yolo.svg?style=for-the-badge)
![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)

<!-- PROJECT LOGO -->
<br />
<h3 align="center">Getting-Acquainted-with-Yolo</h3>

<p align="center">
A growing collection of practical projects to learn and explore the YOLO family of object detection models.
<br />
<a href="https://github.com/Arnav-TheCoder/Getting-Acquainted-with-Yolo"><strong>Explore the repository »</strong></a>
<br />
<br />
<a href="https://github.com/Arnav-TheCoder/Getting-Acquainted-with-Yolo">View Repository</a>
&middot;
<a href="https://github.com/Arnav-TheCoder/Getting-Acquainted-with-Yolo/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
&middot;
<a href="https://github.com/Arnav-TheCoder/Getting-Acquainted-with-Yolo/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
</p>

</div>

<!-- TABLE OF CONTENTS -->

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
      <a href="#repository-structure">Repository Structure</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#learning-roadmap">Learning Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Getting-Acquainted-with-YOLO is a learning-oriented repository built to explore the YOLO (You Only Look Once) family of object detection models through practical projects.

Rather than focusing on a single application, this repository is intended to grow into a collection of progressively more advanced implementations demonstrating how YOLO can be integrated into computer vision workflows using Python, Flask, OpenCV, and modern web technologies.

The objective is to understand not only how to use YOLO models, but also how to build complete AI-powered applications around them.

### Current Progress

#### Image Detection Application

The first project in this repository is a Flask-based image detection application that allows users to:

- Upload an image through a browser interface.
- Detect multiple objects using the YOLO10x model.
- Display bounding boxes around detected objects.
- View confidence scores and bounding box coordinates.
- Compare the original image with the annotated output.

This application serves as the foundation for future YOLO-based projects in this repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

- Python
- Flask
- OpenCV
- HTML
- CSS
- Ultralytics YOLO

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Repository Structure

```text
Getting-Acquainted-with-Yolo
│
├── Image_detection_app/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   ├── uploads/
│   └── results/
│
├── model/
├── requirements.txt
├── README.md
└── .gitignore
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

- Python 3.10 or newer
- Git
- Any Python IDE (PyCharm, VS Code, etc.)

### Installation

```bash
git clone https://github.com/Arnav-TheCoder/Getting-Acquainted-with-Yolo.git
cd Getting-Acquainted-with-Yolo
pip install -r requirements.txt
```

The required YOLO model weights will be downloaded automatically during the first execution if they are not already available.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Currently, the repository contains the Image Detection Application.

Run the application:

```bash
python Image_detection_app/app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Upload an image to perform object detection and visualize the results.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Learning Roadmap

| Project | Status |
|---------|--------|
| Image Detection Application | Completed |
| Webcam Detection Application | In Progress |
| Video Detection | Planned |
| Object Tracking | Planned |
| YOLO Model Comparison | Planned |
| Performance Benchmarking | Planned |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are welcome. If you have a suggestion that would improve the repository, feel free to fork the project, create a feature branch, commit your changes, and open a pull request.

Top contributors:

<a href="https://github.com/Arnav-TheCoder/Getting-Acquainted-with-Yolo/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Arnav-TheCoder/Getting-Acquainted-with-Yolo" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Arnav Ray - arnavr.5610@gmail.com

Project Link: https://github.com/Arnav-TheCoder/Getting-Acquainted-with-Yolo

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

- Ultralytics
- Flask
- OpenCV
- Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>
