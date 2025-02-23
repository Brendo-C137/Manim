from manim import *
import numpy as np
import math

class ChamadaNivelamento(Scene):
    def construct(self):
        svg_logo = SVGMobject("D:\DF\VSCodium\SVGs\SVG\LogoNivelamento.svg").scale(2)
        svg_logo.set_color(WHITE)

        self.add(svg_logo).wait(0.8)
        self.play(FadeOut(svg_logo))

        self.wait(0.2)

        txt = Text("Tem Dificuldade com").to_edge(UP, buff=1)
        txt2 = Text("Matemática?",color="#2357A0").next_to(txt, DOWN)
        equation = MathTex("f(x)=2.\sin(3x\pi)")

        axes = Axes(x_range=[-3, 3], y_range=[-5, 5], axis_config={"color": BLUE}).scale(0.5).next_to(equation, DOWN)
        graph = axes.plot(lambda x: 2*np.sin(3*x*np.pi), color=RED)
        graph_label = axes.get_graph_label(graph, color=BLUE)

        self.play(Write(txt))
        self.play(Write(txt2))
        self.play(Write(equation))
        self.play(Create(axes), Create(graph))
        self.wait(1)

        self.play(FadeOut(txt, txt2, equation, axes, graph))

        svg_pc = SVGMobject("D:\DF\VSCodium\SVGs\SVG\LogoPC.svg").scale(2)
        txt_end = Text("Participe do eixo de").next_to(svg_pc, UP)
        txt_end2 = Text("Pré-Cálculo").set_color_by_gradient("#2357A0").next_to(svg_pc, DOWN)

        self.play(Write(txt_end))
        self.play(Write(txt_end2, run_time=1), FadeIn(svg_pc))
        self.wait(1)
        
        self.play(FadeOut(txt_end), FadeOut(txt_end2), FadeOut(svg_pc))