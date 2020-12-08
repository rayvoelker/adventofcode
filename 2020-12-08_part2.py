from collections import deque

ops = deque()
args = deque()

# with open("2020-12-08_test_input.txt") as input:
# with open("2020-12-08_test_input2.txt") as input:
with open("2020-12-08_input.txt") as input:
    # print(input.readlines().strip("\n"))
    lines = input.read().strip().split("\n")
    for line in lines:
        ops.append(line[:3])
        args.append(int(line[3:]))


# acc increases or decreases a single global value called the accumulator by the value given in the argument.
#   For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction,
#   the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.


class Computer:
    def __init__(self, ops, args):
        """
        expect deque objects for ops and args
        """
        self.acc = 0
        self.ops_run_count = deque([0] * len(ops))
        self.ops = ops
        self.args = args
        self.orig_pos = deque([i for i in range(1, len(ops) + 1)])
        self.prev_ops_run_count = 0
        # after we run this op at orig_pos, set terminate = True
        self.terminate_pos = len(ops)
        self.terminate = False
        return

    def next_op(self):
        """
        executes the op and then moves the deque object along
        """
        if self.ops[0] == "acc":
            """
            acc increases or decreases a single global value called the
            accumulator by the value given in the argument.
            For example, acc +7 would increase the accumulator by 7.
            The accumulator starts at 0. After an acc instruction, the
            instruction immediately below it is executed next.
            """
            self.acc += self.args[0]

            # advance to the next op (and arg)
            self.ops_run_count[0] += 1
            self.prev_ops_run_count = self.ops_run_count[0]
            if self.orig_pos[0] == self.terminate_pos:
                self.terminate = True
            self.orig_pos.rotate(-1)
            self.ops_run_count.rotate(-1)
            self.ops_run_count.rotate(-1)
            self.ops.rotate(-1)
            self.args.rotate(-1)
            return

        if self.ops[0] == "nop":
            """
            nop stands for No OPeration - it does nothing.
            The instruction immediately below it is executed next.
            """
            self.ops_run_count[0] += 1
            self.prev_ops_run_count = self.ops_run_count[0]
            if self.orig_pos[0] == self.terminate_pos:
                self.terminate = True
            self.orig_pos.rotate(-1)
            self.ops_run_count.rotate(-1)
            self.ops.rotate(-1)
            self.args.rotate(-1)
            return

        if self.ops[0] == "jmp":
            rotate_val = self.args[0] * -1
            self.ops_run_count[0] += 1
            self.prev_ops_run_count = self.ops_run_count[0]
            if self.orig_pos[0] == self.terminate_pos:
                self.terminate = True
            self.orig_pos.rotate(rotate_val)
            self.ops_run_count.rotate(rotate_val)
            self.ops.rotate(rotate_val)
            self.args.rotate(rotate_val)

            # print(f"{computer.acc}\n{computer.ops}\n{computer.args}")
            return

        return


# for i in range(len(computer.ops)):
#     computer.next_op()
# print(f"{computer.acc}\n{computer.ops_run_count}\n{computer.ops}\n{computer.args}\n\n")


# get all the "nop" and "jmp" indexes and start swapping and testing
swap_list = [i for i, x in enumerate(ops) if x in ("nop", "jmp")]
for swap in swap_list:
    # print(swap)
    test_ops = ops.copy()
    test_args = args.copy()

    if test_ops[swap] == "jmp":
        test_ops[swap] = "nop"
    else:
        test_ops[swap] = "jmp"

    # re init the computer with the new ops, and a copy of the args
    computer = Computer(test_ops, test_args)

    count = 0
    while not computer.terminate:
        computer.next_op()
        count += 1
        # just kinda brute forcing it here ...
        # original count was 100000 lol
        if count >= 300:
            break
    if computer.terminate:
        print("terminating code found!")
        print(f"steps: \t\t{count}\ncomputer.acc: \t{computer.acc}")
        break
