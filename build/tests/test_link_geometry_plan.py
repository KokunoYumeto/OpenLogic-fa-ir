"""Small adversarial checks, no TeX and no PDF mutation."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import make_link_geometry_probe as probe
from plan_standalone_reference_geometry import braces, horizontal_components


class GeometryPlanTest(unittest.TestCase):
    def test_nested_brace_reader(self):
        self.assertEqual(braces(r'\newlabel{x}{{11.19}{3}{}{target}{}}'),['x','{11.19}{3}{}{target}{}'])

    def test_corrupt_braces_rejected(self):
        for value in ('{x','x}','{{x}'):
            with self.assertRaises(ValueError):braces(value)

    def test_disjoint_foreign_ink_split(self):
        chars=[{'bbox':[10,10,15,20]},{'bbox':[50,10,55,20]}]
        self.assertEqual(horizontal_components(chars,[[30,10,40,20]],[10,10,55,20]),[[10,15],[50,55]])

    def test_blank_space_not_fake_foreign_ink(self):
        chars=[{'bbox':[10,10,15,20]},{'bbox':[20,10,25,20]}]
        self.assertEqual(horizontal_components(chars,[],[10,10,25,20]),[[10,25]])

    def test_other_line_not_foreign_ink(self):
        chars=[{'bbox':[10,10,15,20]},{'bbox':[50,10,55,20]}]
        self.assertEqual(horizontal_components(chars,[[30,30,40,40]],[10,10,55,20]),[[10,55]])

    def test_generator_is_deterministic_and_four_cases(self):
        a=probe.generate()
        self.assertEqual(a,probe.generate())
        self.assertEqual(a.count(b'OL-LINK-GEOMETRY-CASE='),4)
        self.assertEqual(a.count(b'\\hypertarget{fixture.n11.19}'),1)
        self.assertEqual(a.count(b'\\begin{document}'),1)
        self.assertEqual(a.count(b'\\end{document}'),1)


if __name__=='__main__':unittest.main()
