#!/home/kist/PycharmProjects/pythonProject/venv/bin/python
# -*- coding: utf-8 -*-


# import sys
# print("python version", sys.version)
# print("python inter", sys.executable)

import os
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument

import real_time_test


import rospy
from std_msgs.msg import String

import uuid


def talker(text):
    pub = rospy.Publisher('popup_mode', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/kist/catkin_ws/src/pop_up_space/scripts/popup-space-wkbi-2d96eb6b4cb5.json'
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/kist/catkin_ws/src/pop_up_space/scripts/popup1-346908-3c93f93726de.json'

    DIALOGFLOW_PROJECT_ID = 'popup1-346908'
    DIALOGFLOW_LANGUAGE_CODE = 'ko'
    # SESSION_ID = '116492800752545868194'
    SESSION_ID = 'me'

    # while True:
    # 쿼리 input
    text_to_be_analyzed = text
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)




    # dialog 쿼리 output
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("response: ", response.query_result.fulfillment_text)

    hello_str = "%s" % response.query_result.intent.display_name
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()



# talker()
# if __name__ == '__main__':
#     talker(text)
    # try:
    #     talker()
    # except rospy.ROSInterruptException:
    #     pass
