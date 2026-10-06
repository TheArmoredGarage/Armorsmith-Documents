"""Guard public licensing entry points, navigation and cross-surface consistency."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def page(name):
    return (ROOT / f'{name}.mdx').read_text(encoding='utf-8')


def body(text):
    return text.split('---', 2)[2].strip()


def navigation_pages(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key == 'pages':
                yield from (entry for entry in item if isinstance(entry, str))
            else:
                yield from navigation_pages(item)
    elif isinstance(value, list):
        for item in value:
            yield from navigation_pages(item)


class LicensingTests(unittest.TestCase):
    def test_license_and_agreement_are_navigable_once(self):
        config = json.loads((ROOT / 'docs.json').read_text(encoding='utf-8'))
        pages = list(navigation_pages(config['navigation']))
        for name in ('getting-started/licensing', 'getting-started/license-agreement'):
            self.assertEqual(pages.count(name), 1)
            self.assertTrue((ROOT / f'{name}.mdx').is_file())

    def test_every_purchase_entry_point_explains_seats_and_links_policy(self):
        for name in ('index', 'introduction', 'getting-started/installation',
                     'troubleshooting/updates-and-licensing'):
            with self.subTest(page=name):
                text = page(name).lower()
                self.assertRegex(text, r'(each|per|one) (paid seat per )?named individual')
                self.assertIn('/getting-started/licensing', text)
                self.assertIn('studio', text)

    def test_people_and_computers_are_distinguished(self):
        text = page('getting-started/licensing')
        self.assertIn('Six people using Armorsmith require six paid seats', text)
        self.assertIn('even if only two use it at once', text)
        self.assertIn('three-computer allowance is for the same named individual', text)
        self.assertIn('Three different users need three paid seats', text)

    def test_reassignment_is_not_pooling(self):
        text = page('getting-started/licensing')
        self.assertLess(text.index('Remove the previous'), text.index('Update your seat'))
        self.assertIn('Contact The Armored Garage to arrange', text)
        self.assertIn('does not allow daily rotation', text)
        self.assertIn('no self-service studio seat-management interface', text)

    def test_activation_email_is_not_misrepresented_as_user_identity(self):
        for name in ('getting-started/licensing', 'getting-started/installation'):
            self.assertIn('purchase email', page(name).lower())
        self.assertIn('may differ from a studio employee', page('getting-started/licensing'))

    def test_output_receiving_and_trial_exceptions_are_explicit(self):
        text = page('getting-started/licensing')
        self.assertIn('does not by itself require an Armorsmith seat', text)
        self.assertIn('open, view, edit, or export', text)
        self.assertIn('A paid seat is required for production use', text)

    def test_updates_and_earlier_agreements_are_preserved(self):
        for name in ('getting-started/licensing', 'getting-started/license-agreement'):
            text = page(name)
            self.assertIn('All future Armorsmith Designer updates are included', text)
            self.assertIn('do not retroactively replace rights', text)
        self.assertNotIn('more than one computer', page('getting-started/license-agreement'))

    def test_policy_pages_have_valid_frontmatter_and_local_links(self):
        for name in ('getting-started/licensing', 'getting-started/license-agreement'):
            text = page(name)
            self.assertTrue(text.startswith('---\n'))
            self.assertRegex(text, r'title: "[^"]+"')
            self.assertRegex(text, r'description: "[^"]+"')
            for link in re.findall(r'\]\((/[^)#]+)', body(text)):
                self.assertTrue((ROOT / f'{link.lstrip("/")}.mdx').is_file(), link)
        self.assertIn('/getting-started/license-agreement', page('getting-started/licensing'))

    def test_mdx_component_pairs_are_balanced(self):
        for name in ('getting-started/licensing', 'getting-started/installation',
                     'troubleshooting/updates-and-licensing'):
            text = page(name)
            for component in ('Accordion', 'Tip', 'Note', 'Steps', 'Step', 'Warning'):
                opens = len(re.findall(rf'<{component}(?:\s[^>]*|)>', text))
                self.assertEqual(opens, text.count(f'</{component}>'), (name, component))


if __name__ == '__main__':
    unittest.main()
