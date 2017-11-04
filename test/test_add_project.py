from data.projects import testdata
from model.projects import Projects
import pytest


@pytest.mark.parametrize("project", testdata)
def test_add_project(app, project):
    old_project_list = app.project.get_project_list()
    app.project.add_new_project(project)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)
    old_project_list.append(project)
    assert sorted(old_project_list, key=Projects.id_or_max) == sorted(new_project_list, key=Projects.id_or_max)