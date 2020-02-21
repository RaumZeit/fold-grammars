#!/usr/bin/python

import unittest
import os
import subprocess

import tempfile
# import shutil


class Test(unittest.TestCase):

    def setUp(self):
        # os.chdir('/homes/kmaibach/GAPC/fold-grammars/')  # set working directory

        self.fp_workdir = tempfile.mkdtemp()
        os.system('basedir=`pwd` && cd "%s" && gapc -p "alg_dotBracket*alg_count" $basedir/../../nodangle.gap -I $basedir/../../' % self.fp_workdir)
        os.system('basedir=`pwd` && cd "%s" && make -f out.mf CPPFLAGS_EXTRA="-I $basedir/../../"' % self.fp_workdir)

        # self.tmp_dir = tempfile.mkdtemp()  # create temporary directory

        self.sequences = [
            "CCCAa+aaaUGGG",
            "CCCCCCa+auCCCCCaaaGGGGGGGGGGGG",
            "CCC+GGG",
            "UCC+GGG",
            "CCu+GGG",
            "CCC+aCCCaaaGGGGGG",
            "CCU+aCCCaaaGGGGGG",
            "CCC+aUCCaaaGGGGGG",
            "CCC+aCCCCCCaaaGGGGGGGGG",
            "CCC+aUCCCCCaaaGGGGGGGGG",
            "CCC+aUCCCCCaaaGGGGGGGGG",
            "CCC+aUCCCCCaaaGGGGGGGGG",
            "CCCCCCCCCaaaGGGGGGa+GGG",
            "CCCuCCCCCaaaGGGGGGa+GGG",
            "CCCuCCCCCaaaGGGGGGa+GGG",
            "CCCaaCCCCCCaaaGGGGGGa+GGG",
            "CCCaaUCCCCCaaaGGGGGGa+GGG",
            "CCCaaUCCCCCaaaGGGGGGa+GGG",
            "CCCCaaCCCCaa+aGGGGaaGGGGa",
            "CCACCAAAGGACCAAAGGA+GG",
            "GCAUCUGCGUAUCUCGGAUAAUGCAAC+UUGAUAACUAUGCUAUGG",
            "GCAUCUGCGUAUCUCGGAUAAUGCAAC+UUGAUAACUAUGC",
            "CAAUUUAAUCCCCACCGGUCACU+AAAGCCAUUAGG",
            "GGUUUGGGUCUUAAAGGGGCUCUGGGAUACUCCCA+CGGACC",
            "GGUUUAUCGGGUCUUAAAGGGGCUCUGGGAUACUCCCA+CGGACC",
            "GGUUUAUCGGGUCUUAAAGGGGCUCUGGGAUACAUAUUCCCA+CGGACC",
            "GGUUUAUCGGGUGCUUAAAGGGGGCUCUGGGAUACAUAUUCCCA+CGGACC"
            # sequences too long for homes-usage - use on cluster!
            # "GGUUUAUUAGGAUGUCGGGUGCUUAAAGGGGGCUCACGUCUUGGGAUACAUAUUCCCA+CGGACC",
            # "GGACAGACUACAUAGCGAUAUUCGCGAGGGACGGUCCAAGCCAUAAAGAAGACAUUAUGCCAACG+AUCGGUAGAGGCGCUUGCUGAGAUAUCUUUGGUCUUCUAGCGCCUAAGGGCUUCCACACUCCUUGCAUCGUAAAAAUCUAAGAA",
            # "CCACGGAGUUGUACAUCUCCUGUGCGAUGCCCCGCAUCCUGAAUAGGGCAGGUUGCCAGUGGAGGGUUGGGGAUACUUCCGAA+UCCAUAUCCACUCGUGACCGGAGGUUAGUACUUUACGAGCGAAAGGGUGCCCGCGCUUCUUUUCCGGACCCCGCACCACGCAUGUAGAGUACUUGGGAACGAAAGGCCGUAACACGGUGGGACAAAAGCAGCUGCCUAUACGCCGGUUUACCAAGGUCCCCUGGUUGAAUAUCAUGUCUGUGUUGAA",
            # "UAGGAAGAUCGAGUGGCGGCUUCAACCAGGUCGACCCUGUAAAGGGAAGCUUAAAAUCAAGGACCUACCG+UAAUCGUAACUACGCACUAAGCGAAUACGUGGCGAGCCGGA",
            # "GGCACACCCUUGACCGUUUCCUCGUUCCGCUAGCCAACUUACGUGGUGGCAGAUUGGACGGUCAACUAUAUGUGGACAACUAUAAAUUAGUGGAGCGUAGCGACGGAUCUGUAUUGGUACCAGUGU+CCAAACCAGGCUGUCUCGACUCCUGGCC",
            # "GGCCACCCUUGACCGUUUCCUCGUUCCGCUAGCCAACUUACGUGGUGGCAGAUUGGACGGUCAACUAUAUGUGGACAACUAUAAAUUAGUGGAGCGUAGCGACGGAUCUGUAUUGGUACCAGUGU+CCAAACCAGGCUGUCUCGACUCCUGGCC",
            # "GGCCACCCUUGACCGUUUCCUCGUUCCGCUAGCCAACUUACGUGGUGGCAGAUUGGACGGUCAACUAUAUGUGGACAACUAUAAAUUAGUGGAGCGUAGCGACGGUCUGUUGGUACCAGUGU+CCAACAGGCUGUCCGCUCCUGGCC",
            # "GGCCACCCUUGACCGUUUUCCCGCUAGCCAACUUACGUGGUGGGAGGACGGUCAACUAUGUGGACAACUAUAUAGUGGAGCGUAGCGACGGUCUGUUGGUACCAGUGU+CCAACAGGCUGUCCGCUCCUGGCC",
            # "GGCCAUGACCGUUUUCCCGCUAGCCAACUUACGUGGUGGGAGGACGGUCAACUAUGUGGACAACUAUAUAGUGGAGCGGACGGUCUGUUGGUACCAGUGU+CCAACAGGCUGUCCGCUCCUGGCC",
            # "UAGGAAGAUCGAGUGGCGGCUUCAACCAGGUCGACCCUGUAAAGGGAAGCUUAAAAUCAAGGACCUACCG+UAAUCGUAACUACGCACUAAGCGAAUACGUGGCGAGCCGGA",
            # "UAGGAAGAUCGAGUGGCGGCUUCAACCAGGUCGACCCUGUAAAGGGAAGCUUAAAAUCAAGGACCUACCG+UAUGCGACGGUCGCAUGACUUGGCGCUGAGCCAGUCCGCACUUUCGUAAUCGUAACUACGCACUAAGCGAAUACGUGGCGAGCCGGA",
            # "GAAUACAGACAGAGUUAUGAAGGACGCUACGCAUUGUUAAAACGUCGUCUCGUUCAUUGGUCUCGGUUUAUUACGAAAGGAUGUCGGGUGCUUAAAGGGGGCUCACGUCUGACGCCACGCUCAUGGAGCACGCUGGGAUACAUAUUCCCAAUUGUUAGGGCCUGGAAGAC+CGGACCGACCAAGCAU",
            # "UGCUUUGGUCUCUUAGGUUACAGACCAGAUAACGUGCUCUCUUCUCAAGGUGUCAUGGAAAAACGCUUACUAAGAUGAGGAGCGUUGCAUCUGCGUAUCUCGGAUAAUGCAAC+UUGAUAACUAUGCUAUGG",
            # "GGUUUAUUAGGAUGUCGGGUGCUUAAAGGGGGCUCACGUCUAGCACGCUGGGAUACAUAUUCCCAAUUGUU+CGGACC",
            # "GGUUUAUUACGAAAGGAUGUCGGGUGCUUAAAGGGGGCUCACGUCUGACGAGCACGCUGGGAUACAUAUUCCCAAUUGUU+CGGACC",
            # "GGUUUAUUACGAAAGGAUGUCGGGUGCUUAAAGGGGGCUCACGUCUGACGCCACGCUCAUGGAGCACGCUGGGAUACAUAUUCCCAAUUGUUAGGGCCUGGAAGAC+CGGACC",
            # "UGGUCUCGGUUUAUUACGAAAGGAUGUCGGGUGCUUAAAGGGGGCUCACGUCUGACGCCACGCUCAUGGAGCACGCUGGGAUACAUAUUCCCAAUUGUUAGGGCCUGGAAGAC+CGGACCGACCAAGCAU",
            # "GUAGUUGACAGCCCUGAAAUUCGGUCG+CUUUUAAUUAACUCCUUCCUCUUCGGACCGAUGUGCCCUUGGAUAUCCUAUAUGGAAUUUGGUGUCAGGAUUGUGCCAAGGCCACGAACACAGGAAUGCCAUACAA"
        ]

    def tearDown(self):
        pass
        #shutil.rmtree(self.fp_workdir)  # remove temporary directory

    def testUnambiguousness(self):
        for seq in self.sequences:
            # index = self.sequences.index(seq)
            cmd = ('%s/out "%s"' % (self.fp_workdir, seq))
            dot_count = [(subprocess.check_output(cmd, shell=True)).decode("utf-8")]
            # file_name = os.path.join('/homes/kmaibach/GAPC/test/', str(index) + ".txt")
            # file = open(file_name, "w")
            for element in dot_count:
                # file.write(element)
                dot_count_list = element.split('\n')
                # split_list = []
                for el in dot_count_list:
                    if not (el == 'Answer: ' or el == ''):
                        # split_list.append(el.split(",")[1])
                        self.assertEqual(el.split(",")[1], ' 1 )')
            # file.close()


if __name__ == "__main__":
    unittest.main()
