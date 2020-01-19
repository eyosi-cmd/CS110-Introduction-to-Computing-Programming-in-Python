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
        command = "python3 equality.py 5 5 5"
        sought = """equal
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test2(self):
        command = "python3 equality.py 5 1 5"
        sought = """not equal
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem2(unittest.TestCase):

    def test1(self):
        command = "python3 five_per_row.py"
        sought = """101 102 103 104 105
106 107 108 109 110
111 112 113 114 115
116 117 118 119 120
121 122 123 124 125
126 127 128 129 130
131 132 133 134 135
136 137 138 139 140
141 142 143 144 145
146 147 148 149 150
151 152 153 154 155
156 157 158 159 160
161 162 163 164 165
166 167 168 169 170
171 172 173 174 175
176 177 178 179 180
181 182 183 184 185
186 187 188 189 190
191 192 193 194 195
196 197 198 199 200
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem3(unittest.TestCase):

    def test1(self):
        command = "python3 root.py 3 2"
        sought = """1.73205...
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got[:7], sought[:7])

    def test1(self):
        command = "python3 root.py 64 3"
        sought = """4.00000...
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got[:7], sought[:7])

class Problem4(unittest.TestCase):

    def test1(self):
        command = "python3 gcd.py 54 24"
        sought = """6
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test2(self):
        command = "python3 gcd.py 22 45"
        sought = """1
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem5(unittest.TestCase):

    def test1(self):
        command = "python3 prime_counter.py 1000"
        sought = """168
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

if __name__ == "__main__":
    unittest.main()
