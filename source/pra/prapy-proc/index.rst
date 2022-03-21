******************
SFEPRAPY Processor
******************

MCS results of individual simulation case (:literal:`case_name`) are saved in separate CSV files
`.\\mcs.out\\case_name.csv`. Below shows an example of an output file. Rows are iteration, columns are properties.

.. math::

    \begin{matrix}
    \text{index} & \text{beam_position_horizontal} & \text{fire_combustion_efficiency} & ... \\
    318 & 27.35 & 0.96 & ... \\
    1065 & 25.04 & 0.83 & ... \\
    1244 & 20.22 & 0.92 & ... \\
    814 & 19.62 & 0.94 & ... \\
    1276 & 18.75 & 0.82 & ... \\
    ... & ... & ... & ...
    \end{matrix}

Output Properties
=================

.. py:data:: index
    :type: int

    An unique number associated with a MCS iteration.

.. py:data:: beam_position_horizontal
    :type: float

    As per input.

.. py:data:: fire_combustion_efficiency
    :type: float

    As per input.

.. py:data:: fire_hrr_density
    :type: float

    As per input.

.. py:data:: fire_nft_limit
    :type: float

    As per input.

.. py:data:: fire_spread_speed
    :type: float

    As per input.


.. py:data:: window_open_fraction
    :type: float

    As per input.

.. py:data:: fire_load_density
    :type: float

    As per input.

.. py:data:: fire_type
    :type: float

    Indicate the type of design fire selected for the iteration.

    | 0: Parametric fire
    | 1: Travelling fire
    | 2: Parametric fire (DIN)

.. py:data:: solver_steel_temperature_solved
    :type: float

    todo

.. py:data:: solver_time_critical_temp_solved
    :type: float

    todo

.. py:data:: solver_protection_thickness
    :type: float

    Solved protection thickness.

.. py:data:: solver_iter_count
    :type: float

    Number of iterations took to solve the time equivalence.

.. py:data:: solver_time_equivalence_solved
    :type: float

    The solved time equivalence value. This
