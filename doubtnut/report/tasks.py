from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def task1(num1, num2):

    print ("Task 1")
    return num1 + num2

@shared_task
def task2(num1, num2):

    print ("Task 2")

