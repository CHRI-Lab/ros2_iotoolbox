### open three terminal and input the follow command
<hr>
cd ros2_workspace

colcon build

source install/setup.bash

### terminal0 record and publish the path of .wav to /audio_filepath
<hr>
ros2 run my_pac app

### terminal 1 for text analysis
<hr>
ros2 run my_pac demo_node

### terminal 2 for speech to text
<hr>
ros2 run my_pac s_to_t

### open another terminal to wait for result

ros2 topic echo /translated_sentence
