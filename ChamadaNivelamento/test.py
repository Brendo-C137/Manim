from manim import *
import numpy as np

# class teste(Scene):
    # def construct(self)?
        # s = Square()

        # self.play(Create(s))
        
class teste(Scene):
    def construct(self):
        ax = Axes(x_range=[0,6.3]).scale(0.7)
        cir = Circle(color=BLUE).next_to(ax, LEFT)
        sine = ax.plot(lambda x: 2*np.sin(x), color=RED)
        alpha = ValueTracker(0)

        point = always_redraw(lambda: Dot(sine.point_from_proportion(alpha.get_value()),color=BLUE))
        point2 = always_redraw(lambda: Dot(cir.point_from_proportion(alpha.get_value()),color=BLUE))

        
        # tangent = always_redraw(lambda: TangentLine(sine, alpha=alpha.get_value(), color=YELLOW, length=4))
        # self.add(ax, point, point2, cir, sine)
        self.play(Create(ax), Create(cir), Create(sine))
        self.play(Create(point), Create(point2))
        self.play(alpha.animate.set_value(1), rate_func=linear, run_time=2)