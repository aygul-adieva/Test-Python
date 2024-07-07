import pytest
from lesson_8.Pages.TodoMain import Task

zadacha = Task()

def test_todo():
    list = zadacha.get_list()
    assert list.status_code == 200


    params = {"title": "Автоматизация", "completed": 'false'}
    task = zadacha.create(params)

    assert task is not None

    params = {"title": "Автоматизация - крутая штука"}
    renamed_task = zadacha.rename(task, params)

    assert renamed_task.json()['title'] == "Автоматизация - крутая штука"

    info = zadacha.info(task)

    assert info.json() ['title'] == "Автоматизация - крутая штука"

    assert info.json()['id'] == task

    params = {"completed": 'true'}
    status_true = zadacha.change_status(task, params)
    assert status_true == True

    params = {"completed": 'false'}
    status_false = zadacha.change_status(task, params)
    assert status_false == False

    deleting = zadacha.delete(task)
    assert deleting == 204


 
