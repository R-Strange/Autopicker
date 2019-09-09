from behave import *

use_step_matcher("re")


@given("an (.+)")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: Given an <input file>')


@when("we analyse the viability of the file")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we analyse the viability of the file')


@then("we can print any (?P<errors>.+)")
def step_impl(context, errors):
    """
    :type context: behave.runner.Context
    :type errors: str
    """
    raise NotImplementedError(u'STEP: Then we can print any <errors>')


@step("we can (.+) to the next step if it is viable")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: And we can <forward the data> to the next step if it is viable')


@step("we can (.+) if the data is not viable")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: And we can <fail gracefully> if the data is not viable')


@given("a (.+)")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: Given a <viable input file>')


@when("we autopick the data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we autopick the data')


@then("we print back the (.+)")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: Then we print back the <number of found events>')


@step("we produce a (.+) equal to the number of reported events")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: And we produce a <number of event files> equal to the number of reported events')


@step("if we have bad data we (.+)")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: And if we have bad data we <fail gracefully>')