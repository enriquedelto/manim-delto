from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class DivisionEntera(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="es-ES-AlvaroNeural",
                style="serious"
            )
        )

        # Título
        with self.voiceover(text="Comenzamos con el Teorema 1.1: División Entera."):
            title = Text("Teorema 1.1: División Entera", font_size=60)
            self.play(Write(title))
            self.wait(1)
            self.play(title.animate.to_edge(UP))
        
        # a, b \in \mathbb{Z} (grande y centrado)
        with self.voiceover(text="Consideremos dos números enteros a y b."):
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
        with self.voiceover(text="Recordemos que Z es el conjunto de los números enteros que incluye a los negativos, el cero y los positivos sin incluir decimales."):
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
        with self.voiceover(text="Ahora, veamos la condición para b, que indica que b no puede ser 0."):
            b_condition = MathTex(r"b", r"\neq 0").next_to(ab_integers, DOWN, buff=0.5)
            b_condition.set_color_by_tex("b", GREEN)
            self.play(Write(b_condition))
            self.wait(1)

        # Mover ab_integers y b_condition a UL
        ab_and_condition = VGroup(ab_integers, b_condition)
        self.play(ab_and_condition.animate.to_corner(UL))
        self.wait(1)

        # Mostrar q, r \in \mathbb{Z} en el centro de la pantalla
        with self.voiceover(text="Introducimos q y r que también pertenecen al conjunto de los números enteros."):
            qr_integers = MathTex(r"q", r",", r"r", r"\in")
            Z_qr = MathTex(r"\mathbb{Z}").next_to(qr_integers, RIGHT)
            qr_integers.set_color_by_tex("q", YELLOW)
            qr_integers.set_color_by_tex("r", ORANGE)
            qr_group = VGroup(qr_integers, Z_qr).scale(1.5)
            qr_group.move_to(ORIGIN)
            self.play(Write(qr_group))
            self.wait(1)

        # Crear la línea vertical blanca
        separator_line = Line(start=UP * 1, end=DOWN * 1.5, color=WHITE)
        separator_line.next_to(ab_group, RIGHT, buff=0.75)

        # Mover qr_group al lado de ab_group, cambiar su tamaño y mostrar la línea vertical
        self.play(
            qr_group.animate.next_to(separator_line, RIGHT).scale(1/1.5),
            Create(separator_line)
        )
        self.wait(1)

        # q y r aparecen en el centro de la pantalla con definiciones y colores
        tamaño_fuente = 72  # Puedes ajustar este valor según tus preferencias

        with self.voiceover(text="Introducimos q como el coeficiente y r como el resto de la división de a por b.."):
            q_definition = MathTex(r"q", r": \text{coeficiente}", font_size=tamaño_fuente)
            q_definition[0].set_color(YELLOW)

            r_definition = MathTex(r"r", r": \text{resto}", font_size=tamaño_fuente)
            r_definition[0].set_color(ORANGE)

            definitions = VGroup(q_definition, r_definition).arrange(DOWN, buff=0.75)  # Aumenté el buffer para más espacio entre las definiciones
            definitions.move_to(ORIGIN)  # Centra el grupo en la pantalla

            self.play(Write(definitions))
            self.wait(1)
