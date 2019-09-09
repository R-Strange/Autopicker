from behave import *

use_step_matcher("re")


@given("we have data ready for fft analysis")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given we have data ready for fft analysis')


@when("we run an fft extract")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we run an fft extract')


@then("we will produce frequency-domain data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then we will produce frequency-domain data')


@given("we have (.+) data")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: Given we have <frequency-domain> data')


@when("we decibellise the data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we decibellise the data')


@then("we change the data to a (.+)")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: Then we change the data to a <normalised form>')