from manim import *
class Cena1(Scene):
    def construct(self):

        #declare solar system and auxiliary objects
        earth = Dot(color=BLUE, fill_opacity=1.0).scale(2).shift(3.5*UP)
        sun = Circle(color=YELLOW, radius=1, fill_color=YELLOW, fill_opacity=1)
        orbit = Circle(color=WHITE, radius=3.5, stroke_width=2)
        half_orbit = Arc(radius=3.5, angle=PI, stroke_width=0).rotate(PI/2, about_point=sun.get_center())
        system = VGroup(earth, sun, orbit, half_orbit).shift(3*RIGHT)
        star = Dot().shift(6*LEFT)
        
        desc_earth = Tex("Terra", color=BLUE).next_to(earth, DOWN)
        desc_sun = Tex("Sol", color=YELLOW).next_to(sun, UP)
        desc_star = Tex("estrela").next_to(star, UP)
        
        
        #create solar system
        self.wait(1)
        self.play(DrawBorderThenFill(sun), Write(orbit), FadeIn(earth, shift=UP), run_time=1)
        self.play(Write(desc_earth), Write(desc_sun))
        self.play(Write(star), Write(desc_star))
        self.add_foreground_mobjects(star, earth)
        self.wait()
        self.play(FadeOut(desc_earth), FadeOut(desc_sun), FadeOut(desc_star))

        #declare and create lines from earth to the star at different moments
        linha = DashedLine().add_updater(lambda x:
                                   x.become(Line(earth.get_center(), star.get_center(), stroke_width=3)))
        linha1 = linha.copy()
        self.play(DrawBorderThenFill(linha), DrawBorderThenFill(linha1), run_time=1.5)
        linha1.clear_updaters()
        self.play(linha1.animate.set_color(GREEN), run_time=0.5)
        self.wait(1)

        self.play(MoveAlongPath(earth,half_orbit), run_time=1.5)
        
        linha2 = linha.copy()
        self.add(linha2)
        linha2.clear_updaters()
        self.play(linha2.animate.set_color(GREEN), run_time=0.5)
        self.remove(linha)
        self.wait(0.5)

        #move and scale down solar system
        linha1.add_updater(lambda x:
                           x.become(Line(orbit.get_top(), star.get_center(), stroke_width=3, color=GREEN)))
        linha2.add_updater(lambda x:
                           x.become(Line(orbit.get_bottom(), star.get_center(), stroke_width=3, color=GREEN)))
        self.add_foreground_mobjects(linha1, linha2, star)
        self.play(system.animate.scale(0.25).shift(2*RIGHT), run_time=2)

        #declare and create auxiliary lines, angle and equation
        d = DashedLine(star, sun, stroke_width=2, color=WHITE, dash_length=0.02)
        desc_d = MathTex("D").next_to(linha2, DOWN).set_color(GREEN).shift(3*RIGHT)
        paral = Angle(d, linha1, radius=5, stroke_width=3, color = BLUE, quadrant=(1, -1))
        theta = MathTex("\\theta").next_to(paral, UP).set_color(BLUE)
        ex = Tex("para $\\theta$ \\\ muito pequenos:").scale(1.5).to_edge(UP).shift(3*LEFT)
        eq1 = MathTex("D = \\frac{1}{\\theta}").scale(2).to_edge(UP).shift(2*RIGHT)
        eq2 = Tex("$\\theta$ em arco-segundos \\\ D em parsecs").to_edge(DOWN, buff=2).set_color(GREY).shift(3*LEFT)
        ex[0][4].set_color(BLUE)
        eq1[0][4].set_color(BLUE)
        eq1[0][0].set_color(GREEN)
        eq2[0][0].set_color(BLUE)
        eq2[0][16].set_color(GREEN)
        
        self.play(LaggedStart(Write(d), FadeOut(earth), lag_ratio=0.5), run_time=1.5)
        self.play(LaggedStart(Write(desc_d), Write(paral), Write(theta), FadeIn(ex), Write(eq1), FadeIn(eq2), lag_ratio=0.8))
        self.wait(2)
