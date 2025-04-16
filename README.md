# Smart Home using M5Stack Core2

## 1. Introduction 
In this project, I use M5Stack and TMOS IR sensor to automate the handling of air conditioner and lights like turn on or turn off when motion was detected in the room. Moreover, with the collected data (at least 2 weeks), this system will provide an optimized plan to automate the handling of home appliances, even if no motion is detected. For example, this system will automatically turn on the air conditioner 30 minutes before you come home.

## 2. Components Required:
1. M5Stack Core2
2. M5STACK-U185　[Link](https://www.switch-science.com/collections/m5stack/products/9927)
3. SwitchBot Hub Plus
4. AWS (Database and Server)

## 3. Method

As you can see in Figure 1, the system is based on Core2 and TMOS IR sensor. Then, using SwitchBot Hub to control home apliances.

![alt text](/Fig/IoT-Final-Project.png)
<p align ="center" >Figure 1. Smart Home using M5Stack Core2</p>

### 3.1. Motion detecting Module
This module detect motions in the room using the TMOS IR sensor. You may not know, humans emit infrared radiation in the form of heat, and infrared (IR) sensors and thermal sensors, such as the TMOS or other infrared thermal sensors, can detect changes in temperature to identify motion. In this module, It will analyze the temperature changes in the thermal image provided by the IR sensor. A sudden change in the pixel values can be considered as a motion.

### 3.2. Home Appliances Controlling Module
This module controll home appliances, such as air conditioners or LED bulbs through Infrared (IR) Communication. However, Core2 doesn't have this feature. In this module, I use SwitchBot Hub Plus which support many installed home appliances , and also allow to manually adding unknown devices. All commands will be sent from Core2 through the API. 

### 3.3. Storing Data
The motion detection data and the state (on, off) of home appliances will be stored in the cloud for optimization. This system not only controls home appliances when motion is detected in the room, but also operates them even if no motion is detected. For example, with the collected data, the system will predict when will you be in the room, and turn on the air conditioner 30 minutes before that.

### 3.4. Optimization (researching....)
