### open three terminal and input the follow command
___

cd ros2_workspace

colcon build

source install/setup.bash

### terminal0 record and publish the path of .wav to /audio_filepath
___

ros2 run my_pac app

### terminal 1 for text analysis
___

ros2 run my_pac demo_node

### terminal 2 for speech to text
___

ros2 run my_pac s_to_t

### open another terminal to wait for result
___

ros2 topic echo /translated_sentence
