# 'If Elif Statements'

"If-else" can only produce 2 possible branches.

Ideally, you should be able to branch as many times as needed.

For example, you might need to check a test score and then report its grade equivalent.

You could still do this with a series of nested if-else statements. This is not ideal because excessively nested statements are to be avoided because they are difficult to debug.

#### Python has an "elif" statement that we can use instead. Here is a pseudocode representation of elif:
        if <boolean condition>:
            # some action
        elif <boolean condition>:
            # some other action
        elif <boolean condition>:
            # some other, other action
              |
              |
        else:
            # another action

Any number of elif statements can be used.

Also, elif must always end with an else clause.
