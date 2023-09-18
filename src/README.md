# open two terminal and input the follow command
cd ros2_workspace

colcon build

source install/setup.bash


# terminal 1 for text analysis

ros2 run my_pac demo_node

# terminal 2 for speech to text

ros2 run my_pac s_to_t

# open another terminal to wait for result

ros2 topic echo /translated_sentence

# publish the path of .wav

ros2 topic pub --once /audio_filepath std_msgs/msg/String "data: '/home/nsc/ros2_workspace/src/voice/test1.wav'"
