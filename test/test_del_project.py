from model.projects import Projects
from random import randrange


def test_del_project(app):
    if len(app.soap.get_project_list()) == 0:
        app.project.add_new_project(Projects(name="name", description="test"))
    old_project_list = app.soap.get_project_list()
    index = randrange(len(old_project_list))
    app.project.delete_any_project(index)
    new_project_list = app.soap.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    del old_project_list[index]
    assert sorted(old_project_list, key=Projects.id_or_max) == sorted(new_project_list, key=Projects.id_or_max)