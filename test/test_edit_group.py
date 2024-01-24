from model.group import Group


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group(name="New name", header="New header", footer="New footer"))
    app.session.logout()
