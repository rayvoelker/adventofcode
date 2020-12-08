from collections import deque

ops = deque()
args = deque()

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
        expect a deque object
        """
        self.acc = 0
        self.ops_run_count = deque([0] * len(ops))
        self.ops = ops
        self.args = args
        self.prev_ops_run_count = 0

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
            self.ops_run_count.rotate(-1)
            self.ops.rotate(-1)
            self.args.rotate(-1)
            return

        if self.ops[0] == "jmp":
            rotate_val = self.args[0] * -1
            self.ops_run_count[0] += 1
            self.prev_ops_run_count = self.ops_run_count[0]
            self.ops_run_count.rotate(rotate_val)
            self.ops.rotate(rotate_val)
            self.args.rotate(rotate_val)
            # print(f"{computer.acc}\n{computer.ops}\n{computer.args}")
            return

        return


# for i in range(len(computer.ops)):
#     computer.next_op()
# print(f"{computer.acc}\n{computer.ops_run_count}\n{computer.ops}\n{computer.args}\n\n")


computer = Computer(ops, args)

acc = computer.acc
while True:
    computer.next_op()
    if computer.prev_ops_run_count >= 2:
        break
    acc = computer.acc

print(f"{computer.acc}\n{computer.ops_run_count}\n{computer.ops}\n{computer.args}\n\n")

print(acc)
