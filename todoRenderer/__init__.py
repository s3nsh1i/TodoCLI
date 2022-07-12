from textual.widget import Widget
from textual.views import GridView
from rich.console import group, RenderableType
from rich.panel import Panel
from rich.align import Align
from rich.layout import Layout
from .components.Task import Task
from .components.SubmitBtn import Submit
from .components.InputText import InputText


class TodoLayout(Widget):
    def __init__(self, todo, *args):
        super().__init__(*args)
        self.todo = todo

    def render(self) -> RenderableType:
        grid = Layout()
        grid.split_column(
            Layout(Panel(Align.center('[bold]Tasks avaliables[/]')), size=4, ratio=3),
            Layout(Panel(self.load_tasks())),
        )

        return (grid)


    @group()
    def load_tasks(self):
        for task_data in self.todo['tasks']:
            yield Task(task_data['name'], task_data['status'])


class ActionsLayout(GridView):
    def __init__(self, color):
        super().__init__()
        self.color = color

    async def on_mount(self) -> None:
        self.command_field = InputText('Command')

        self.grid.set_align('center', 'center')
        self.grid.set_gap(True, True)

        self.grid.add_column(name='input')
        self.grid.add_column(size=20, name='button')
        self.grid.add_row("row", repeat=1, size=3)

        self.grid.add_widget(self.command_field)
        self.grid.add_widget(Submit('Submit', self.color))

