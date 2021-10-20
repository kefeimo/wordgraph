import unittest
from utils.token import TokenizerV1
from utils.definition import DefinitionRetrieverFromWN
from utils.dependency import *


class TestRawDependencySelectorFromWN(unittest.TestCase):

    def test_calc_dependencies(self):
        dep = RawDependencySelectorFromWN()
        word = "module"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(
            {'electronic', 'item', 'assembly', 'unit', 'a', 'one', 'is', ')', 'component', 'that', 'compartment',
             'self-contained', 'in', 'mind', 'as', 'consisting', 'or', 'spacecraft', 'the', 'circuit', 'combination',
             'other', 'perceptual', 'of', 'components', 'with', 'used', '(', 'inherent', 'an', 'computer', 'hardware',
             'detachable', 'powers', 'cognitive'}),
            dep.calc_dependencies(word))

    def test_calc_dependencies_2(self):
        dep = RawDependencySelectorFromWN()
        word = "module123432"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(), dep.calc_dependencies(word))


class TestLegalDependencySelectorFromWN(unittest.TestCase):

    def test_calc_dependencies(self):
        dep = LegalDependencySelectorFromWN()
        word = "module"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(
            {'in', 'consisting', 'self-contained', 'detachable', 'used', 'electronic', 'one', 'mind', 'component', 'or',
             'assembly', 'other', 'as', 'hardware', 'cognitive', 'an', 'compartment', 'a', 'spacecraft', 'perceptual',
             'item', 'is', 'circuit', 'computer', 'combination', 'components', 'powers', 'unit', 'inherent'}),
            dep.calc_dependencies(word))

    def test_calc_dependencies_2(self):
        dep = LegalDependencySelectorFromWN()
        word = "module123432"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(), dep.calc_dependencies(word))


class TestRawDependencySelectorFromDict(unittest.TestCase):

    def test_calc_dependencies(self):
        dep = RawDependencySelectorFromDict()
        word = "module"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(
            {'consisting', 'with', 'that', 'mind', 'assembly', 'spacecraft', 'an', 'a', 'powers', 'self-contained',
             'perceptual', 'unit', 'in', 'compartment', 'cognitive', 'circuit', 'hardware', 'is', 'component',
             'detachable', 'computer', 'or', 'combination', '(', 'the', 'item', 'as', 'one', ')', 'electronic',
             'components', 'inherent', 'used', 'other', 'of'}),
            dep.calc_dependencies(word))

    def test_calc_dependencies_2(self):
        dep = RawDependencySelectorFromDict()
        word = "module123432"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(), dep.calc_dependencies(word))


class TestLegalDependencySelectorFromDict(unittest.TestCase):

    def test_calc_dependencies(self):
        dep = LegalDependencySelectorFromDict()
        word = "module"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(
            {'self-contained', 'unit', 'electronic', 'compartment', 'one', 'an', 'inherent', 'in', 'assembly', 'mind',
             'detachable', 'perceptual', 'as', 'item', 'used', 'combination', 'component', 'or', 'circuit', 'a',
             'hardware', 'other', 'computer', 'cognitive', 'spacecraft'}),
            dep.calc_dependencies(word))

    def test_calc_dependencies_2(self):
        dep = LegalDependencySelectorFromDict()
        word = "module123432"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(), dep.calc_dependencies(word))


class TestRawDependencySelectorFast(unittest.TestCase):

    def test_calc_dependencies(self):
        dep = RawDependencySelectorFromDict()
        word = "module"
        print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(
            {'consisting', 'with', 'that', 'mind', 'assembly', 'spacecraft', 'an', 'a', 'powers', 'self-contained',
             'perceptual', 'unit', 'in', 'compartment', 'cognitive', 'circuit', 'hardware', 'is', 'component',
             'detachable', 'computer', 'or', 'combination', '(', 'the', 'item', 'as', 'one', ')', 'electronic',
             'components', 'inherent', 'used', 'other', 'of'}),
            RawDependencySelectorFast.calc_dependencies(word))

    def test_calc_dependencies_2(self):
        dep = RawDependencySelectorFromDict()
        word = "module123432"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(), RawDependencySelectorFast.calc_dependencies(word))


class TestLegalDependencySelectorFast(unittest.TestCase):

    # def test_calc_dependencies(self):
    #     dep = LegalDependencySelectorFromDict()
    #     word = "module"
    #     # print(dep.calc_dependencies(word))
    #     self.assertEqual(frozenset(
    #         {'self-contained', 'unit', 'electronic', 'compartment', 'one', 'an', 'inherent', 'in', 'assembly', 'mind',
    #          'detachable', 'perceptual', 'as', 'item', 'used', 'combination', 'component', 'or', 'circuit', 'a',
    #          'hardware', 'other', 'computer', 'cognitive', 'spacecraft'}),
    #         LegalDependencySelectorFast.calc_dependencies(word))

    def test_calc_dependencies_2(self):
        dep = LegalDependencySelectorFromDict()
        word = "module123432"
        # print(dep.calc_dependencies(word))
        self.assertEqual(frozenset(), LegalDependencySelectorFast.calc_dependencies(word))


# =====================
# default
class TestDependencyRawSpannerFast(unittest.TestCase):

    def test_span_dependencies(self):
        dep_spanner = RawDependencySpannerFast()
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        self.assertEqual(
            {'in', 'disperse', 'hard', 'inoculate', 'inspiration', 'stages', 'rounds', 'testa', 'early', 'by', 'ground',
             ';', 'will', 'from', 'one', 'embryo', 'having', 'containing', 'a', 'an', 'source', 'later', 'sprinkle',
             'bear', 'help', 'remove', 'future', 'work', 'for', 'to', 'protective', 'that', 'mature', 'fertilized',
             'food', 'not', 'silver', 'fluid', 'so', 'with', 'anything', 'microorganisms', 'money', 'the', 'teams',
             'cause', 'is', 'thick', 'tract', 'growth', 'rain', 'white', 'enterprise', 'development', 'provides',
             'ejaculated', 'and', ')', 'on', 'genital', '(', 'particles', 'spermatozoa', 'seeds', 'fruit', 'coat',
             'meet', 'consisting', 'of', 'place', 'or', 'players', 'iodide', 'distribute', 'plant', 'ovule', 'seed',
             'its', 'outstanding', 'male', 'go', 'small', 'shed', 'providing', 'tournament'},
            RawDependencySpannerFast.span_dependencies(seed, 1)[0])

    def test_span_dependencies_multidepth(self):
        dep_spanner = RawDependencySpannerFast()
        seed = "cognition"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        self.assertEqual(
            {'gain', 'skills', 'become', 'something', 'effort', ')', 'gained', 'making', 'consequence', 'certainty',
             'etc', 'component', ',', 'determine', 'how', 'have', 'subject', 'verb', 'problem', 'cognition', 'issue',
             'emotional', 'with', 'certain', 'the', 'physical', 'get', 'is', ';', 'phrase', 'aware', 'concept', 'find',
             '.', 'of', 'activity', 'be', '(', 'explains', 'only', 'phenomenon', 'reasons', 'reason', 'logical',
             'virtue', 'knowledge', 'representation', 'commit', 'noun', 'know', 'specified', 'memory', 'and',
             'scholarly', 'accidentally', 'relating', 'arguments', 'conclusion', 'end', 'to', 'perceived', 'role',
             'clause', 'a', 'formation', 'psychological', 'by', 'present', 'logically', 'denoted', 'results',
             'referent', 'come', 'that', 'learn', 'thinking', 'terminate', 'statement', 'cognitive', 'in', 'perceiving',
             'state', 'previous', 'skill', 'psychology', 'inquiry', 'semantic', 'residue', 'coherent', 'acquiring',
             'think', 'determined', 'student', 'capacity', 'heart', 'perception', 'opposed', 'endowed', 'learning',
             'exists', 'whose', 'impart', 'nature', 'becoming', 'caused', 'usually', 'decide', 'process', 'as', 'what',
             'mental', 'solves', 'follows', 'senses', 'profound', 'reasoning', 'basic', 'some', 'follow', 'via', 'or',
             'solve', 'out', 'conceiving', 'result', 'about', 'an', 'way', 'draw', 'other'},
            RawDependencySpannerFast.span_dependencies(seed, 2)[0])

    def test_span_dependencies_converge(self):
        dep_spanner = RawDependencySpannerFast
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        res = RawDependencySpannerFast.span_dependencies(seed, 30)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))
        res = RawDependencySpannerFast.span_dependencies(seed, 3)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))


# default
class TestDependencyLegalSpannerFast(unittest.TestCase):
    dep_spanner = LegalDependencySpannerFast()

    def test_span_dependencies(self):
        dep_spanner = LegalDependencySpannerFast()
        seed = "seed"
        # print(self.dep_spanner.span_dependencies(seed, 1)[0])
        self.assertEqual(
            {'sprinkle', 'development', 'genital', 'inoculate', 'an', 'players', 'is', 'containing', 'tournament',
             'ovule', 'silver', 'inspiration', 'its', 'rounds', 'outstanding', 'ejaculated', 'white', 'a',
             'spermatozoa', 'one', 'small', 'bear', 'iodide', 'fruit', 'seed', 'in', 'place', 'tract', 'growth', 'shed',
             'stages', 'go', 'later', 'testa', 'rain', 'will', 'teams', 'seeds', 'thick', 'money', 'hard', 'disperse',
             'future', 'so', 'or', 'male', 'having', 'fertilized', 'mature', 'remove', 'cause', 'by', 'distribute',
             'microorganisms', 'embryo', 'provides', 'work', 'not', 'food', 'consisting', 'on', 'plant', 'meet',
             'fluid', 'help', 'enterprise', 'particles', 'ground', 'early', 'protective', 'source', 'coat',
             'providing'},
            self.dep_spanner.span_dependencies(seed, 1)[0])

    def test_span_dependencies_multidepth(self):
        dep_spanner = LegalDependencySpannerFast()
        seed = "cognition"
        # print(self.dep_spanner.span_dependencies(seed, 2)[0])
        self.assertEqual(
            {'logical', 'relating', 'aware', 'emotional', 'certainty', 'other', 'decide', 'determined', 'explains',
             'capacity', 'role', 'physical', 'phenomenon', 'arguments', 'come', 'previous', 'component', 'heart',
             'solves', 'end', 'have', 'activity', 'knowledge', 'results', 'student', 'scholarly', 'reasoning', 'reason',
             'follow', 'phrase', 'representation', 'mental', 'inquiry', 'making', 'state', 'usually', 'referent',
             'psychology', 'gain', 'verb', 'draw', 'thinking', 'think', 'nature', 'psychological', 'problem', 'skill',
             'be', 'is', 'certain', 'consequence', 'conclusion', 'coherent', 'logically', 'determine', 'commit', 'find',
             'by', 'result', 'concept', 'accidentally', 'perception', 'denoted', 'specified', 'reasons', 'exists',
             'become', 'caused', 'semantic', 'profound', 'learn', 'or', 'only', 'an', 'solve', 'present', 'virtue',
             'some', 'conceiving', 'perceived', 'memory', 'follows', 'about', 'becoming', 'a', 'residue', 'learning',
             'formation', 'skills', 'in', 'process', 'way', 'terminate', 'acquiring', 'effort', 'out', 'noun',
             'cognition', 'perceiving', 'know', 'clause', 'impart', 'gained', 'issue', 'basic', 'as', 'get', 'subject',
             'opposed', 'cognitive', 'endowed', 'statement', 'senses'},
            self.dep_spanner.span_dependencies(seed, 2)[0])

    def test_span_dependencies_converge(self):
        dep_spanner = RawDependencySpannerFast
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        res = LegalDependencySpannerFast.span_dependencies(seed, 30)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))
        res = LegalDependencySpannerFast.span_dependencies(seed, 3)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))


class TestDependencyRawSpannerFastV2(unittest.TestCase):
    dep_spanner = LegalDependencySpannerFastV2()

    def test_span_dependencies_converge(self):
        dep_spanner = RawDependencySpannerFast
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        res = self.dep_spanner.span_dependencies(seed, 30)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))
        res = self.dep_spanner.span_dependencies(seed, 3)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))


class TestDependencyLegalSpannerFastV2(unittest.TestCase):
    dep_spanner = LegalDependencySpannerFastV2()

    # def test_span_dependencies(self):
    #     seed = "seed"
    #     # print(LegalDependencySpannerFast.span_dependencies(seed, 1)[0])
    #     self.assertEqual(
    #         {'coat', 'small', 'money', 'early', 'genital', 'or', 'one', 'development', 'iodide', 'place', 'on',
    #          'growth', 'work', 'source', 'meet', 'male', 'go', 'tournament', 'testa', 'thick', 'protective', 'fluid',
    #          'rain', 'disperse', 'inspiration', 'a', 'ovule', 'silver', 'sprinkle', 'fruit', 'help', 'not', 'shed',
    #          'later', 'tract', 'inoculate', 'plant', 'outstanding', 'in', 'hard', 'by', 'food', 'seed', 'future',
    #          'ground', 'white', 'remove', 'cause', 'bear', 'embryo', 'mature', 'an', 'will', 'distribute', 'so',
    #          'enterprise'},
    #         self.dep_spanner.span_dependencies(seed, 1)[0])

    # def test_span_dependencies_multidepth(self):
    #     dep_spanner = LegalDependencySpannerFast()
    #     seed = "cognition"
    #     # print(dep_spanner.span_dependencies(seed, 2)[0])
    #     self.assertEqual(
    #         {'get', 'commit', 'psychology', 'opposed', 'profound', 'accidentally', 'making', 'know', 'logical',
    #          'subject', 'acquiring', 'other', 'representation', 'find', 'or', 'physical', 'aware', 'be', 'have',
    #          'reason', 'terminate', 'in', 'semantic', 'verb', 'way', 'draw', 'knowledge', 'sens', 'argument', 'process',
    #          'referent', 'present', 'a', 'by', 'clause', 'conclusion', 'emotional', 'perceived', 'noun', 'become',
    #          'activity', 'think', 'problem', 'determined', 'basic', 'capacity', 'out', 'some', 'skill', 'scholarly',
    #          'determine', 'cognition', 'solve', 'impart', 'only', 'specified', 'phrase', 'becoming', 'decide',
    #          'thinking', 'issue', 'end', 'heart', 'concept', 'perception', 'usually', 'an', 'effort', 'consequence',
    #          'gain', 'endowed', 'virtue', 'formation', 'learning', 'component', 'logically', 'mental', 'phenomenon',
    #          'follow', 'coherent', 'learn', 'certainty', 'psychological', 'residue', 'statement', 'memory', 'reasoning',
    #          'role', 'previous', 'nature', 'student', 'result', 'state', 'cognitive', 'come', 'about', 'certain',
    #          'inquiry'},
    #         LegalDependencySpannerFastV2.span_dependencies(seed, 2)[0])

    def test_span_dependencies_converge(self):
        dep_spanner = RawDependencySpannerFast
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        res = LegalDependencySpannerFastV2.span_dependencies(seed, 30)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))
        res = LegalDependencySpannerFastV2.span_dependencies(seed, 3)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))


class TestDependencyRawSpannerFromDict(unittest.TestCase):

    def test_span_dependencies(self):
        dep_spanner = RawDependencySpannerFromDict()
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        self.assertEqual(
            {'in', 'disperse', 'hard', 'inoculate', 'inspiration', 'stages', 'rounds', 'testa', 'early', 'by', 'ground',
             ';', 'will', 'from', 'one', 'embryo', 'having', 'containing', 'a', 'an', 'source', 'later', 'sprinkle',
             'bear', 'help', 'remove', 'future', 'work', 'for', 'to', 'protective', 'that', 'mature', 'fertilized',
             'food', 'not', 'silver', 'fluid', 'so', 'with', 'anything', 'microorganisms', 'money', 'the', 'teams',
             'cause', 'is', 'thick', 'tract', 'growth', 'rain', 'white', 'enterprise', 'development', 'provides',
             'ejaculated', 'and', ')', 'on', 'genital', '(', 'particles', 'spermatozoa', 'seeds', 'fruit', 'coat',
             'meet', 'consisting', 'of', 'place', 'or', 'players', 'iodide', 'distribute', 'plant', 'ovule', 'seed',
             'its', 'outstanding', 'male', 'go', 'small', 'shed', 'providing', 'tournament'},
            RawDependencySpannerFromDict.span_dependencies(seed, 1)[0])

    def test_span_dependencies_multidepth(self):
        dep_spanner = RawDependencySpannerFromDict()
        seed = "cognition"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        self.assertEqual(
            {'gain', 'skills', 'become', 'something', 'effort', ')', 'gained', 'making', 'consequence', 'certainty',
             'etc', 'component', ',', 'determine', 'how', 'have', 'subject', 'verb', 'problem', 'cognition', 'issue',
             'emotional', 'with', 'certain', 'the', 'physical', 'get', 'is', ';', 'phrase', 'aware', 'concept', 'find',
             '.', 'of', 'activity', 'be', '(', 'explains', 'only', 'phenomenon', 'reasons', 'reason', 'logical',
             'virtue', 'knowledge', 'representation', 'commit', 'noun', 'know', 'specified', 'memory', 'and',
             'scholarly', 'accidentally', 'relating', 'arguments', 'conclusion', 'end', 'to', 'perceived', 'role',
             'clause', 'a', 'formation', 'psychological', 'by', 'present', 'logically', 'denoted', 'results',
             'referent', 'come', 'that', 'learn', 'thinking', 'terminate', 'statement', 'cognitive', 'in', 'perceiving',
             'state', 'previous', 'skill', 'psychology', 'inquiry', 'semantic', 'residue', 'coherent', 'acquiring',
             'think', 'determined', 'student', 'capacity', 'heart', 'perception', 'opposed', 'endowed', 'learning',
             'exists', 'whose', 'impart', 'nature', 'becoming', 'caused', 'usually', 'decide', 'process', 'as', 'what',
             'mental', 'solves', 'follows', 'senses', 'profound', 'reasoning', 'basic', 'some', 'follow', 'via', 'or',
             'solve', 'out', 'conceiving', 'result', 'about', 'an', 'way', 'draw', 'other'},
            RawDependencySpannerFromDict.span_dependencies(seed, 2)[0])

    def test_span_dependencies_converge(self):
        dep_spanner = RawDependencySpannerFromDict
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        res = RawDependencySpannerFromDict.span_dependencies(seed, 30)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))
        res = RawDependencySpannerFromDict.span_dependencies(seed, 3)
        # print(list(map(len, res)))
        self.assertEqual(True, len(res[1]) + 1 == len(res[2]))


class TestDependencyLegalSpannerFromDict(unittest.TestCase):

    def test_span_dependencies(self):
        dep_spanner = LegalDependencySpannerFromDict()
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        self.assertEqual(
            {'growth', 'tournament', 'distribute', 'enterprise', 'remove', 'cause', 'in', 'small', 'fruit', 'so',
             'source', 'future', 'early', 'protective', 'white', 'later', 'shed', 'outstanding', 'testa', 'rain',
             'genital', 'ground', 'or', 'work', 'go', 'on', 'money', 'male', 'food', 'a', 'tract', 'inoculate', 'plant',
             'hard', 'mature', 'thick', 'help', 'silver', 'fluid', 'not', 'sprinkle', 'one', 'ovule', 'by', 'meet',
             'place', 'development', 'an', 'inspiration', 'bear', 'will', 'iodide', 'coat', 'embryo', 'seed',
             'disperse'},
            dep_spanner.span_dependencies(seed, 1)[0])


class TestDependencyRawSpannerFromWN(unittest.TestCase):

    def test_span_dependencies(self):
        dep_spanner = RawDependencySpannerFromWN()
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        self.assertEqual(
            {'(', 'iodide', 'development', 'bear', 'providing', 'ground', 'later', 'seed', 'embryo', 'fertilized',
             'microorganisms', 'genital', 'go', 'plant', 'anything', 'sprinkle', 'mature', 'or', 'distribute', 'having',
             ')', 'a', 'consisting', 'help', 'containing', 'an', 'from', 'food', 'remove', 'will', 'testa',
             'inspiration', 'male', 'future', 'tract', 'with', 'inoculate', 'seeds', ';', 'teams', 'provides', 'place',
             'on', 'ovule', 'and', 'outstanding', 'so', 'early', 'its', 'thick', 'hard', 'coat', 'the', 'protective',
             'rain', 'growth', 'meet', 'of', 'fruit', 'source', 'stages', 'one', 'disperse', 'white', 'is', 'shed',
             'in', 'by', 'fluid', 'for', 'money', 'particles', 'spermatozoa', 'tournament', 'to', 'small', 'not',
             'work', 'that', 'ejaculated', 'cause', 'rounds', 'enterprise', 'players', 'silver'},
            dep_spanner.span_dependencies(seed, 1)[0])


class TestDependencyLegalSpannerFromWN(unittest.TestCase):

    def test_span_dependencies(self):
        dep_spanner = LegalDependencySpannerFromWN()
        seed = "seed"
        # print(dep_spanner.span_dependencies(seed, 1)[0])
        self.assertEqual(
            {'embryo', 'its', 'players', 'go', 'white', 'sprinkle', 'coat', 'protective', 'shed', 'iodide',
             'inspiration', 'remove', 'development', 'bear', 'so', 'ovule', 'later', 'help', 'fluid', 'microorganisms',
             'silver', 'rounds', 'on', 'seed', 'thick', 'will', 'particles', 'small', 'genital', 'mature', 'place',
             'food', 'testa', 'money', 'an', 'fruit', 'is', 'cause', 'a', 'early', 'distribute', 'ejaculated',
             'inoculate', 'in', 'consisting', 'stages', 'future', 'growth', 'work', 'tournament', 'having', 'provides',
             'rain', 'male', 'disperse', 'ground', 'outstanding', 'tract', 'fertilized', 'one', 'by', 'not',
             'spermatozoa', 'providing', 'meet', 'source', 'enterprise', 'hard', 'teams', 'or', 'seeds', 'containing',
             'plant'},
            dep_spanner.span_dependencies(seed, 1)[0])
