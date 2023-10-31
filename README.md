# AI-RedBack
## About project
The aim of this project is to develop a ROS2-based platform to enable the integration of voice commands and information recognized by the robot's vision and to operate the robot.   
The project members are listed below:  

## Contributors

| Name        | Student ID | Role              | Contact                         |
|-------------|------------|-------------------|---------------------------------|
| Renwei Hu   | 1067974    | Product Owner     | renweih@student.unimelb.edu.au  |
| Sicheng Nie | 1206202    | Scrum Master      | sichengn@student.unimelb.edu.au |
| George Wang | 1084224    | Architecture Lead | wagw@student.unimelb.edu.au     |
| Siyi Liu    | 710301     | Deployment Lead   | siyil6@student.unimelb.edu.au   |

## Working Process
The project is divided into four modules based on prioritization:  
- Computer Vision
- Voice Command Recognition
- Decision Making
- Robotic Control
We will develop them in order.  

### Naming rules
Sprint tag: `COMP90082_2023_SM2_AI_RedBack_BL_SPRINTX`
Branch Naming Convention: `<user_story_id>-<"feature/bug_fix">-<person>-<description>`

## Progress Demos
All demos reflecting our project progress have been uploaded to a [YouTube Playlist](https://www.youtube.com/playlist?list=PL1DAddnTedRfXLiYhuk05oO45_SJ-DaV0). Demo video for each independent module can also be accessed via direct links below:
- [Object Detection](https://youtu.be/aJUBKjuEKGA)
- [Human Gesture](https://youtu.be/93jVHLQO9h8)
- [Speech to Text](https://youtu.be/3NdqpdoMN8E)

## Repo
The project is mainly divided into two repos: [AI RedBack](https://github.com/COMP90082-2023-SM2/AI-RedBack) and [AI RedBack Vision](https://github.com/COMP90082-2023-SM2/AI-RedBack-Vision)(Client requested). AI RedBack has all the sprint documents and Voice Recognition content, while AI RedBack Vision mainly focuses on Vision.

## Environment Set Up
### ROS2(Humble) Installation Guide
- Official documentation can be found here: https://docs.ros.org/en/humble/Installation.html  
- Confluence guide document: This [link](https://confluence.cis.unimelb.edu.au:8443/display/COMP900822023SM2AIRedBack/ROS+2+%28Humble%29+Installation+Guide) will guide you to install the ROS2.

### Libfranka Installation Guide
- Official documentation can be found here: https://frankaemika.github.io/docs/installation_linux.html
- Confluence guide document: This [link](https://confluence.cis.unimelb.edu.au:8443/display/COMP900822023SM2AIRedBack/Libfranka+Installation+Guide) will guide you to install the Libfranka.

### Franka_ros2 Installation Guide
- Official documentation can be found here: https://support.franka.de/docs/franka_ros2.html
- Confluence guide document: This [link](https://confluence.cis.unimelb.edu.au:8443/display/COMP900822023SM2AIRedBack/Franka_ros2+Installation+Guide) will guide you to install the Franka_ros2.

## Changelog
### Voice Recognition
- Version Oct 6, 2023
  - Updated semantic analysis ROS2 node to capture more information. Updated the recording app to enable it to start and end recording using space operations

- Version Sep 21, 2023
  - Upload the ROS2 node version of the application used for recording voice and update the document

- Version Sep 18, 2023
  - Upload ROS2 Python node files for voice to text conversion and their test. wav files

- Version Sep 6, 2023
  - Upload ROS2 python node

- Version Sep 3, 2023
  - Upload Python files for semantic analysis using OpenAI

- Version Aug 18, 2023
  - Upload documents related to sprint 1

- Version Aug 16, 2023
  - Create Github repo

## Openai Prompt
### Grammar correct
"Please correct the grammar of the following text: \"{transcript}\""
### Text Analysis
"Translate the sentence into action, object and location, for example a sentence 'slowly move that red cup to the top of the table' should be 'Action: slowly move; Object: red cup; Location: top of the table'. If there is no location information, Location should be N/A. Now please translate {sentence}"

## File List
This [file](https://github.com/COMP90082-2023-SM2/AI-RedBack/blob/VR1.8-auto_script-easten/docs/sprint3/file.txt) contains all the file list.
