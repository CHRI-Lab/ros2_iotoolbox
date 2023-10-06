## Step-by-step instructions
Please make sure that you have installed the ROS2 environment and created a Python package named 'my_pac,' and placed the three Python files inside 'my_pac/my_pac'.

### update setup.py
The code snippet for 'console_scripts' in the code is to be modified as follows:

```python
'console_scripts': [
      'demo_node = my_pac.demo_node:main',
	    's_to_t = my_pac.s_to_t:main',
	    'app = my_pac.app:main'
	
        ],
```
___
### open three terminal and input the follow command

cd ros2_workspace

colcon build

source install/setup.bash
___
### terminal 0 record and publish the path of .wav to /audio_filepath

ros2 run my_pac app
___
### terminal 1 for speech to text

ros2 run my_pac s_to_t
___
### terminal 2 for text analysis

ros2 run my_pac demo_node
___
### open another terminal to wait for result

ros2 topic echo /translated_sentence

file 'nodes_launch.py' was not found in the share directory of package 'my_pac' which is at '/home/nsc/ros2_workspace/install/my_pac/share/my_pac'

## Auto Script

cd ros2_workspace  
colcon build  
source install/setup.bash  
ros2 launch my_pac nodes_launch.py  
