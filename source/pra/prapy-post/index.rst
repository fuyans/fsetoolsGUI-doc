SFEPRAPY Post Processor
***********************

::

    root
    ├── input.xslx
    └── msc.out
        ├── case_a.csv
        ├── case_b.csv
        └── case_c.csv

Output Parameters in Individual Case
====================================

.. object:: index

    [:math:`1`] A unique unsigned integer assigned to simulation iteration.

.. object:: beam_position_horizontal

    [:math:`m`] The structural element's horizontal position relative to fire ignition location.

.. object:: fire_combustion_efficiency

    [:math:`1`] The fire combustion efficiency

.. object:: fire_hrr_density

    [:math:`MW/m^2`] todo

.. object:: fire_nft_limit

    [:math:`^oC`] todo

.. object:: fire_spread_speed

    [:math:`m/s`] todo

.. object:: window_open_fraction

    [:math:`1`] todo

.. object:: fire_load_density

    [:math:`MJ/m^2`] todo

.. object:: fire_type

    | :math:`0`: parametric fire
    | :math:`1`: travelling fire
    | :math:`2`: parametric fire (din)

.. object:: extinction

    [:math:`s`], is the fuel depletion time. This is estimated differently as per below depending on `fire_type`.

    | :math:`\text{fire_type}=0`: None.
    | :math:`\text{fire_type}=1`: When the back of travelling fire reaches the end of the floor plate.
    | :math:`\text{fire_type}=2`: This is effectively the :math:`t_2_x` parameter in the correlation.

.. object:: solver_steel_temperature_solved

    [:math:`^oC`]

.. object:: solver_time_critical_temp_solved

    [:math:`s`]

.. object:: solver_protection_thickness

    [:math:`m`]

.. object:: solver_iter_count

    [:math:`1`]

.. object:: solver_time_equivalence_solved

    [:math:`s`]
