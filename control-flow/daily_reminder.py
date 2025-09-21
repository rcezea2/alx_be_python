#!/usr/bin/python3

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == 'yes':
            print('Reminder: {} is a {} priority task that'
                  ' requires immediate attention today!'.format(task, priority))
        elif time_bound == 'no':
            print('Note: {} is a {} priority task. Consider'
                  ' completing it when you have free time.'.format(task, priority))
    case 'medium':
        if time_bound == 'yes':
            print('Reminder: {} is a {} priority task that'
                  ' requires immediate attention today!'.format(task, priority))
        elif time_bound == 'no':
            print('Note: {} is a {} priority task. Consider'
                  ' completing it when you have free time.'.format(task, priority))
    case 'low':
        if time_bound == 'yes':
            print('Reminder: {} is a {} priority task that'
                  ' requires immediate attention today!'.format(task, priority))
        elif time_bound == 'no':
            print('Note: {} is a {} priority task. Consider'
                  ' completing it when you have free time.'.format(task, priority))
