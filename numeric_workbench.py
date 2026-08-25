"""
The Numeric Workbench
======================
A terminal toolkit that turns your original all-in-one calculator into a
step-by-step, pictorial experience. Nothing is dumped on screen all at once —
each answer is built up in front of you, the way you'd work it out by hand.

Requires:  pip install rich
Run with:  python numeric_workbench.py
"""

import time
import random
import math

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, FloatPrompt, Confirm
from rich.align import Align
from rich.rule import Rule
from rich import box

console = Console()

# A small pause between "steps" so the answer feels worked-out, not dumped.
STEP_DELAY = 0.45


def beat(seconds: float = STEP_DELAY) -> None:
    """One pause between animation steps."""
    time.sleep(seconds)


def reveal(renderable, delay: float = STEP_DELAY) -> None:
    """Print one piece of the picture, then pause before the next."""
    console.print(renderable)
    beat(delay)


# ----------------------------------------------------------------------
# Calculate: the same operations as your original class, each one now
# drawing its answer step by step instead of printing a single line.
# ----------------------------------------------------------------------
class Calculate:
    def __init__(self):
        self.number = 0.0

    # ---------- Number basics ----------

    def even_odd(self):
        n = self.number
        console.print(f"[dim]Checking whether {n:g} splits evenly into pairs...[/dim]")
        beat()
        if not float(n).is_integer():
            reveal("[bold red]That's not a whole number — evenness only applies to integers.[/bold red]")
            return
        n = int(n)
        remainder = n % 2
        reveal(f"  {n} ÷ 2  →  remainder [bold]{remainder}[/bold]")
        if remainder == 0:
            reveal(f"[bold green]{n} is EVEN[/bold green]  {'●' * min(n if n>0 else 1, 20)}")
        else:
            reveal(f"[bold yellow]{n} is ODD[/bold yellow]  {'●' * min(n if n>0 else 1, 20)}")

    def number_line(self):
        n = self.number
        width = 21  # -10 .. 10 visual window, clamps large numbers to the edges
        center = width // 2
        pos = center + max(-center, min(center, round(n)))
        line = ["─"] * width
        line[center] = "0"
        line[pos] = "●"
        reveal(Panel("".join(line), title="Number line", box=box.ROUNDED))
        if n > 0:
            reveal(f"[green]{n:g} is Positive[/green] — sits to the right of zero.")
        elif n < 0:
            reveal(f"[red]{n:g} is Negative[/red] — sits to the left of zero.")
        else:
            reveal(f"[cyan]{n:g} is Zero[/cyan] — sits right on the mark.")

    def factorial(self):
        n = self.number
        if not float(n).is_integer() or n < 0:
            reveal("[bold red]Factorial only works for whole numbers 0 or greater.[/bold red]")
            return
        n = int(n)
        if n > 20:
            reveal(f"[yellow]{n}! grows huge — showing the final value only (skipping the chain).[/yellow]")
            result = math.factorial(n)
            reveal(f"[bold]{n}! = {result}[/bold]")
            return
        if n == 0:
            reveal("[bold]0! = 1[/bold]  (defined that way, by convention)")
            return
        chain = str(n)
        total = n
        for i in range(n - 1, 0, -1):
            total *= i
            chain += f" × {i}"
            reveal(f"  {chain}  =  [bold]{total}[/bold]")
        reveal(f"[bold green]{n}! = {total}[/bold green]")

    # ---------- Shapes ----------

    def area_of_circle(self):
        r = self.number
        reveal(self._circle_art(r))
        reveal(f"  Area = π × r²  =  3.14 × {r:g}²")
        beat()
        reveal(f"[bold green]Area = {3.14 * r * r:.4f}[/bold green]")

    def circumference_of_circle(self):
        r = self.number
        reveal(self._circle_art(r))
        reveal(f"  Circumference = 2 × π × r  =  2 × 3.14 × {r:g}")
        beat()
        reveal(f"[bold green]Circumference = {2 * 3.14 * r:.4f}[/bold green]")

    def _circle_art(self, r):
        size = max(3, min(11, round(abs(r)) or 3))
        mid = size // 2
        rows = []
        for y in range(size):
            row = ""
            for x in range(size):
                d = math.hypot(x - mid, y - mid)
                row += "●" if abs(d - mid) < 0.9 else " "
            rows.append(row)
        return Panel("\n".join(rows), title=f"radius ≈ {r:g}", box=box.ROUNDED)

    def area_of_sq(self):
        s = self.number
        reveal(self._square_art(s))
        beat()
        reveal(f"[bold green]Area = {s:g} × {s:g} = {s*s:.4f}[/bold green]")

    def perimeter_of_sq(self):
        s = self.number
        reveal(self._square_art(s))
        beat()
        reveal(f"[bold green]Perimeter = 4 × {s:g} = {4*s:.4f}[/bold green]")

    def _square_art(self, s):
        side = max(2, min(12, round(abs(s)) or 2))
        row = "■ " * side
        return Panel("\n".join([row.strip()] * side), title=f"side ≈ {s:g}", box=box.ROUNDED)

    def sq(self):
        n = self.number
        reveal(f"  {n:g} × {n:g}")
        beat()
        reveal(f"[bold green]{n:g}² = {n*n:.6f}[/bold green]")

    def cube(self):
        n = self.number
        reveal(f"  {n:g} × {n:g} × {n:g}")
        beat()
        reveal(f"[bold green]{n:g}³ = {n**3:.6f}[/bold green]")

    # ---------- Roots ----------

    def sq_root_of_a_number(self):
        n = self.number
        if n < 0:
            reveal("[bold red]Negative numbers don't have a real square root.[/bold red]")
            return
        guess = n / 2 if n else 0
        reveal(f"[dim]Homing in on √{n:g}...[/dim]")
        for _ in range(4):
            if guess == 0:
                break
            guess = (guess + n / guess) / 2
            reveal(f"  approximation → {guess:.6f}")
        reveal(f"[bold green]√{n:g} = {math.sqrt(n):.6f}[/bold green]")

    def cube_root(self):
        n = self.number
        sign = -1 if n < 0 else 1
        result = sign * (abs(n) ** (1 / 3))
        reveal(f"[dim]Solving x³ = {n:g}...[/dim]")
        beat()
        reveal(f"[bold green]∛{n:g} = {result:.6f}[/bold green]")

    # ---------- Everyday math ----------

    def gpa_calculator(self):
        score = self.number
        bands = [(85, 100, "4.0"), (80, 84, "3.7"), (75, 79, "3.3"),
                 (70, 74, "3.0"), (65, 69, "2.7"), (60, 64, "2.3")]
        filled = max(0, min(40, round(score * 0.4)))
        bar = "█" * filled + "░" * (40 - filled)
        reveal(Panel(f"[bold]{bar}[/bold]\n0{' '*36}100", title=f"score: {score:g}", box=box.ROUNDED))
        for lo, hi, grade in bands:
            marker = " ← you" if lo <= score <= hi else ""
            reveal(f"  {lo:>3}–{hi:<3}  →  GPA {grade}{marker}")
        for lo, hi, grade in bands:
            if lo <= score <= hi:
                reveal(f"[bold green]Your GPA is {grade}[/bold green]")
                return
        reveal("[bold yellow]That's below every band — better luck next time![/bold yellow]")

    def leap_year(self):
        year = self.number
        if not float(year).is_integer():
            reveal("[bold red]Years are whole numbers — try something like 2024.[/bold red]")
            return
        year = int(year)
        reveal(f"[dim]Rule: divisible by 4, and not by 100 unless also by 400.[/dim]")
        by4 = year % 4 == 0
        reveal(f"  {year} ÷ 4 exact? [{'green' if by4 else 'red'}]{by4}[/{'green' if by4 else 'red'}]")
        if not by4:
            reveal(f"[bold red]{year} is NOT a leap year[/bold red]")
            return
        by100 = year % 100 == 0
        by400 = year % 400 == 0
        if by100:
            reveal(f"  {year} ÷ 100 exact? [yellow]{by100}[/yellow] → also check ÷ 400")
            reveal(f"  {year} ÷ 400 exact? [{'green' if by400 else 'red'}]{by400}[/{'green' if by400 else 'red'}]")
        is_leap = by4 and (not by100 or by400)
        if is_leap:
            reveal(f"[bold green]{year} IS a leap year — February gets 29 days.[/bold green]")
        else:
            reveal(f"[bold red]{year} is NOT a leap year.[/bold red]")

    def temp_category(self):
        t = self.number
        levels = max(0, min(20, round((t + 10) / 3)))
        thermometer = "\n".join(
            ["  ┃ ┃  "] * max(0, 20 - levels) +
            [" ▐█▌  "] * levels +
            ["  ●●   "]
        )
        reveal(Panel(thermometer, title=f"{t:g}°C", box=box.ROUNDED))
        if t >= 35:
            reveal("[bold red]It's Hot! Take sunglasses.[/bold red]")
        elif 25 <= t <= 34:
            reveal("[bold yellow]It's Moderate! Be happy.[/bold yellow]")
        else:
            reveal("[bold cyan]It's Cold! Stay covered, stay safe.[/bold cyan]")

    # ---------- For fun ----------

    def random_number(self):
        guess = self.number
        reveal("[dim]Drawing a secret number between 1 and 100...[/dim]")
        for dots in range(3):
            console.print("." * (dots + 1), end="\r")
            beat(0.35)
        target = random.randint(1, 100)
        console.print(" " * 10, end="\r")
        if round(guess) == target:
            reveal(f"[bold green]You guessed {guess:g} — the secret number WAS {target}. You won![/bold green]")
        else:
            reveal(f"[bold]You guessed {guess:g}.[/bold] The secret number was [bold]{target}[/bold]. Not a match — try again!")

    def table(self):
        n = self.number
        t = Table(box=box.SIMPLE_HEAVY, show_header=True, header_style="bold")
        t.add_column(f"{n:g} ×", justify="right")
        t.add_column("=", justify="center")
        for i in range(1, 11):
            t.add_row(str(i), f"{n*i:g}")
            console.print(t)
            beat(0.18)
            console.clear()
        console.print(t)


# ----------------------------------------------------------------------
# Menu: same 16 operations as your original, grouped for readability,
# with a pictorial banner and a persistent loop.
# ----------------------------------------------------------------------
MENU = [
    ("Number basics", [
        ("1", "Even or Odd", "even_odd"),
        ("12", "Positive / Negative / Zero", "number_line"),
        ("2", "Factorial", "factorial"),
    ]),
    ("Shapes", [
        ("4", "Area of a Circle", "area_of_circle"),
        ("5", "Circumference of a Circle", "circumference_of_circle"),
        ("6", "Area of a Square", "area_of_sq"),
        ("7", "Perimeter of a Square", "perimeter_of_sq"),
        ("15", "Square", "sq"),
        ("16", "Cube", "cube"),
    ]),
    ("Roots", [
        ("9", "Square Root", "sq_root_of_a_number"),
        ("14", "Cube Root", "cube_root"),
    ]),
    ("Everyday math", [
        ("3", "GPA Calculator", "gpa_calculator"),
        ("8", "Leap Year Check", "leap_year"),
        ("13", "Temperature Category", "temp_category"),
    ]),
    ("For fun", [
        ("10", "Number Guessing Game", "random_number"),
        ("11", "Multiplication Table", "table"),
    ]),
]

CHOICE_TO_METHOD = {code: method for _, ops in MENU for code, _, method in ops}
CHOICE_TO_LABEL = {code: label for _, ops in MENU for code, label, _ in ops}


def banner():
    console.clear()
    title = Text("THE NUMERIC WORKBENCH", style="bold white on dark_green", justify="center")
    sub = Text("one tool at a time — worked out step by step", style="italic dim", justify="center")
    console.print(Panel(Align.center(title), box=box.DOUBLE, style="green"))
    console.print(Align.center(sub))
    console.print()


def show_menu():
    table = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
    table.add_column(justify="right", style="bold cyan", width=4)
    table.add_column()
    for group_name, ops in MENU:
        table.add_row("", f"[bold]{group_name}[/bold]")
        for code, label, _ in ops:
            table.add_row(code, label)
        table.add_row("", "")
    table.add_row("0", "[dim]Exit[/dim]")
    console.print(table)


def run():
    calc = Calculate()
    while True:
        banner()
        show_menu()
        choice = Prompt.ask("\n[bold]Enter your choice[/bold]", default="0")

        if choice == "0":
            if Confirm.ask("Are you sure you want to exit?", default=False):
                console.print("\n[dim]Closed the workbench. See you next time.[/dim]\n")
                return
            continue

        if choice not in CHOICE_TO_METHOD:
            console.print("[red]That's not on the pad — pick a number from the list.[/red]")
            beat(0.9)
            continue

        label = CHOICE_TO_LABEL[choice]
        console.print(Rule(f"[bold]{label}[/bold]", style="green"))

        if choice == "10":
            prompt_label = "Your guess (1–100)"
        elif choice == "8":
            prompt_label = "Year"
        else:
            prompt_label = "Your number"

        calc.number = FloatPrompt.ask(prompt_label)
        console.print()

        method = getattr(calc, CHOICE_TO_METHOD[choice])
        method()

        console.print()
        Prompt.ask("[dim]Press Enter to return to the menu[/dim]", default="")


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        console.print("\n[dim]Closed the workbench.[/dim]")
