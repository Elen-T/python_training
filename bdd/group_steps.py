from pytest_bdd import given, when, then

@given('a group list')
def group_list():
    pass

@when('I add a new group')
def add_new_group(app):
    app.group.create(group)

@then('the new group list is equal to the old list with the added group')
def verify_group_added():
    pass
