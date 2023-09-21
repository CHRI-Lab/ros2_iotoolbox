### open three terminal and input the follow command

cd ros2_workspace

colcon build

source install/setup.bash
___
### terminal 0 record and publish the path of .wav to /audio_filepath

ros2 run my_pac app
___
### terminal 1 for text analysis

ros2 run my_pac demo_node
___
### terminal 2 for speech to text


ros2 run my_pac s_to_t
___
### open another terminal to wait for result

ros2 topic echo /translated_sentence
