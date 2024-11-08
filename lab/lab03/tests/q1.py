test = {
  'name': 'Question 1: Tricky Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def f(x):
          ...     return x * x
          >>> g = lambda x: f(x + 1)
          >>> g
          7de6c49bc14c42a377b0db3edef26769
          # locked
          >>> g(1)
          ddaa7a9319ef243f9a2b64d17a9e980b
          # locked
          >>> print(g(2))
          fd28f2215ca71dd46d365e63078e8152
          # locked
          >>> f = lambda x: f(x + 1)
          >>> f(1)    # When is the return expression of a lambda expression executed?
          62784451e2ca298dd496ac8954d0a003
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def f1(n):
          ...     def f2(x):
          ...         if x == 0:
          ...             return 'cake'
          ...         else:
          ...             print('The cake is a lie.')
          ...             n -= x
          ...             return f2(n)
          ...     return f2
          >>> f1(2)
          7de6c49bc14c42a377b0db3edef26769
          # locked
          >>> f1(2)(2)
          d6d4372fd234df28a887d36a8da7f3e6
          62784451e2ca298dd496ac8954d0a003
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
