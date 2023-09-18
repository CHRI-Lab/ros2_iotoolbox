cd ros2_workspace
colcon build
source install/setup.bash

ros2 run my_pac demo_node
ros2 topic pub --once /input_sentence std_msgs/msg/String "data: 'Pick up that apple'"
ros2 topic echo /translated_sentence

ros2 run my_pac s_to_t
ros2 topic pub --once /audio_filepath std_msgs/msg/String "/src/1.wav"
ros2 topic echo /corrected_text
