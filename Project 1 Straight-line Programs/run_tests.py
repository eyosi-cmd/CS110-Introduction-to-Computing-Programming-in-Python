import datetime, os, signal, subprocess, sys, time, unittest

def run(command, stdin = None, timeout = 30):
    """
    Runs the specified command using specified standard input (if any) and
    returns the output on success. If the command doesn't return within the
    specified time (in seconds), "__TIMEOUT__" is returned.
    """

    start = datetime.datetime.now()
    process = subprocess.Popen(command.split(),
                               stdin = subprocess.PIPE, 
                               stdout = subprocess.PIPE,
                               stderr = subprocess.STDOUT)
    if not stdin is None:
        process.stdin.write(bytes(stdin, 'utf-8'))
    process.stdin.close()
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return "__TIMEOUT__"
    result = process.stdout.read().decode("utf-8")
    process.stdout.close()
    return result

class Problem1(unittest.TestCase):

    def test1(self):
        command = "python3 wind_chill.py 32 15"
        sought = """21.588988890532022
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem2(unittest.TestCase):

    def test1(self):
        command = "python3 bmi.py 75 1.83"
        sought = """22.395413419331717
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem3(unittest.TestCase):

    def test1(self):
        command = "python3 polar.py 1 1"
        sought = """1.4142135623730951
0.7853981633974483
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem4(unittest.TestCase):

    def test1(self):
        command = "python3 order_check.py 2 4 5"
        sought = """True
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test2(self):
        command = "python3 order_check.py 2 5 4"
        sought = """False
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test3(self):
        command = "python3 order_check.py 5 4 2"
        sought = """True
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem5(unittest.TestCase):

    def test1(self):
        command = "python3 day_of_week.py 3 14 1879"
        sought = """5
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem6(unittest.TestCase):

    def test1(self):
        command = "python3 mercator.py 0 42.36 -71.06"
        sought = """-71.06 0.8176461519422712
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem7(unittest.TestCase):

    def test1(self):
        command = "python3 great_circle.py 48.87 -2.33 37.8 -122.4"
        sought = """8701.389543238289
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem8(unittest.TestCase):

    def test1(self):
        command = "python3 three_sort.py 1 2 3"
        sought = """1 2 3
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
    
    def test2(self):
        command = "python3 three_sort.py 1 3 2"
        sought = """1 2 3
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test3(self):
        command = "python3 three_sort.py 2 1 3"
        sought = """1 2 3
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test4(self):
        command = "python3 three_sort.py 2 3 1"
        sought = """1 2 3
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test5(self):
        command = "python3 three_sort.py 3 1 2"
        sought = """1 2 3
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test6(self):
        command = "python3 three_sort.py 3 2 1"
        sought = """1 2 3
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem9(unittest.TestCase):

    def test1(self):
        command = "python3 random_int.py 10 20"
        got = int(run(command))
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertTrue(got >= 10 and got < 20)

class Problem10(unittest.TestCase):

    def test1(self):
        command = "python3 three_dice.py"
        got = int(run(command))
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertTrue(got >= 3 and got <= 18)

if __name__ == "__main__":
    unittest.main()
