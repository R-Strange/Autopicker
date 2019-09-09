from behave import *

use_step_matcher("re")


@given("we have an event")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given we have an event')


@when("we run it through an AI")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we run it through an AI')


@then("the AI will flag the event for us")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the AI will flag the event for us')


@given("we have noise")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given we have noise')


@then("the AI will not flag the event for us")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the AI will not flag the event for us')