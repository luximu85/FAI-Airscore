from factory import PostGenerationMethodCall, Sequence, Factory
from factory.faker import faker
import task
from formula import TaskFormula
from participant import Participant
from pilot import Pilot
from track import Track
from flightresult import FlightResult
from notification import Notification
from route import Turnpoint
from datetime import date
from random import random
from myconn import Database
import comp


class DBFactory(Factory):
    """db factory"""
    class Meta:
        model = Database


class TaskFactory(Factory):
    """Task factory"""
    class Meta:
        model = task.Task

    task_id = 1
    comp_id = 1


class TurnpointFactory(Factory):
    """Turnpoint factory"""
    class Meta:
        model = Turnpoint


    name = Sequence(lambda n: f"TP{n}")
    description = faker.Faker().sentence(nb_words=4)
    altitude = int(random()*1000)
    shape = 'circle'
    type = 'waypoint'
    how = 'entry'


class CompFactory(Factory):
    """Comp factory"""
    class Meta:
        model = comp.Comp


class TaskFormulaFactory(Factory):
    """TaskFormula factory"""
    class Meta:
        model = TaskFormula


class PilotFactory(Factory):
    """Pilot factory"""
    class Meta:
        model = Pilot


class TrackFactory(Factory):
    """Track factory"""
    class Meta:
        model = Track


class Flight_resultFactory(Factory):
    """FlightResult factory"""
    class Meta:
        model = FlightResult


class ParticipantFactory(Factory):
    """Participant factory"""
    class Meta:
        model = Participant


class NotificationFactory(Factory):
    """Notification factory"""
    class Meta:
        model = Notification
