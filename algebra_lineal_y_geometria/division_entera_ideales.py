from manim import *

class DivisionEntera(Scene):
    def construct(self):
        # Título
        title = Text("Teorema 1.1: División Entera", font_size=60)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # a, b \in \mathbb{Z} (grande y centrado)
        ab_integers = MathTex(r"a", r",", r"b", r"\in")
        Z = MathTex(r"\mathbb{Z}").next_to(ab_integers, RIGHT)
        ab_integers.set_color_by_tex("a", BLUE)
        ab_integers.set_color_by_tex("b", GREEN)
        ab_integers.set_color_by_tex(r"\in", WHITE)
        ab_group = VGroup(ab_integers, Z).scale(1.5)
        ab_group.move_to(ORIGIN)
        self.play(Write(ab_group))
        self.wait(1)

        # Desvanecer título y mover ab_group a UL
        self.play(FadeOut(title))
        self.play(ab_group.animate.scale(1/1.5).to_corner(UL))
        self.wait(1)

        # Mover Z hacia el centro y hacerla crecer
        self.play(Z.animate.move_to(ORIGIN).shift(LEFT * 4).scale(1.5))
        self.wait(1)

        # Secuencia "= (...,-3,-2,-1,0,1,2,3,...)"
        num_sequence = MathTex(r" = (...,-3,-2,-1,0,1,2,3,...)", font_size=60).next_to(Z, RIGHT, buff=0.2)
        num_elements = len(num_sequence[0])
        for i in range(num_elements):
            color = interpolate_color(BLUE, GREEN, i / num_elements)
            num_sequence[0][i].set_color(color)
        self.play(Write(num_sequence))
        self.wait(1)

        # Desvanecer la secuencia de números
        self.play(FadeOut(num_sequence))

        # Z vuelve a la ecuación
        Z_target_position = ab_integers.get_right() + RIGHT * 0.4
        self.play(Z.animate.move_to(Z_target_position).scale(1/1.5))
        ab_group = VGroup(ab_integers, Z)
        self.wait(1)

        # Mostrar b \neq 0 (misma coloración para b)
        b_condition = MathTex(r"b", r"\neq 0").next_to(ab_integers, DOWN, buff=0.5)
        b_condition.set_color_by_tex("b", GREEN)
        self.play(Write(b_condition))
        self.wait(1)

        # Mover ab_integers y b_condition a UL
        ab_and_condition = VGroup(ab_integers, b_condition)
        self.play(ab_and_condition.animate.to_corner(UL))
        self.wait(1)
