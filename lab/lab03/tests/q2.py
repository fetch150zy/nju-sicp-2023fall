test = {
  'name': 'Question 2: Squared Virahanka Fibonacci',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def virfib_sq(n):
          ...     print(n)
          ...     if n <= 1:
          ...         return n
          ...     return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2
          >>> virfib_sq
          7de6c49bc14c42a377b0db3edef26769
          # locked
          >>> r0 = virfib_sq(0)
          0ba991824de5e8e95670d0ffe0c53ea4
          # locked
          >>> virfib_sq(1)
          a18c4ea8c75c25aee4dbd35a59a6fe3d
          a18c4ea8c75c25aee4dbd35a59a6fe3d
          # locked
          >>> r1 = virfib_sq(1)
          a18c4ea8c75c25aee4dbd35a59a6fe3d
          # locked
          >>> r2 = virfib_sq(2)
          062f3edda9181361294b4636ea574132
          a18c4ea8c75c25aee4dbd35a59a6fe3d
          0ba991824de5e8e95670d0ffe0c53ea4
          # locked
          >>> r3 = virfib_sq(3)
          555c3de3e983dc51d8a2a34a9d07c586
          062f3edda9181361294b4636ea574132
          a18c4ea8c75c25aee4dbd35a59a6fe3d
          0ba991824de5e8e95670d0ffe0c53ea4
          a18c4ea8c75c25aee4dbd35a59a6fe3d
          # locked
          >>> r3
          ddaa7a9319ef243f9a2b64d17a9e980b
          # locked
          >>> (r1 + r2) ** 2
          ddaa7a9319ef243f9a2b64d17a9e980b
          # locked
          >>> r4 = virfib_sq(4)
          ddaa7a9319ef243f9a2b64d17a9e980b
          555c3de3e983dc51d8a2a34a9d07c586
          062f3edda9181361294b4636ea574132
          a18c4ea8c75c25aee4dbd35a59a6fe3d
          0ba991824de5e8e95670d0ffe0c53ea4
          a18c4ea8c75c25aee4dbd35a59a6fe3d
          062f3edda9181361294b4636ea574132
          a18c4ea8c75c25aee4dbd35a59a6fe3d
          0ba991824de5e8e95670d0ffe0c53ea4
          # locked
          >>> r4
          f53474ff836c5de3ebe56eee38694363
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
