******************
SFEPRAPY Processor
******************

Input File
==========

A input file should be a spreadsheet file in CSV or *.xlsx format. Below shows an example.

.. math::

    \begin{matrix}
    \text{case_name}                & \text{case_name_a}    & \text{case_name_b}    & ... \\
    \text{n_simulations}            & 2500                  & 2500                  & ... \\
    \text{fire_time_step}           & 10                    & 10                    & ... \\
    \text{fire_time_duration}       & 18000                 & 18000                 & ... \\
    \text{fire_hrr_density:dist}    & \text{uniform_}       & \text{uniform_}       & ... \\
    \text{fire_hrr_density:lbound}  & 0.249                 & 0.249                 & ... \\
    \text{fire_hrr_density:ubound}  & 0.251                 & 0.251                 & ... \\
    \text{fire_load_density:mean}   & \text{gumbel_r_}      & \text{gumbel_r_}      & ... \\
    \text{fire_load_density:sd}     & 10                    & 10                    & ... \\
    ...                             & ...                   & ...                   & ...
    \end{matrix}

The first column are the required input parameters by the time equivalence Monte Carlo simulation routine.
The other columns are input parameters of specific simulation cases. There is no limits on the number of simulation
cases.

Input parameters, their description, data type and dimensions are documented below.

.. py:data:: case_name
    :type: str

    An unique name for a simulation case. It should be unique among all simulation cases. This will be used as a file
    name to save MCS outputs, thus it should be file name safe on the operating system.

.. py:data:: fire_mode
    :type: int

    Should be an integer from 0 to 4, inclusive. To define what design fires to use:

    | 0 - Only to use Eurocode parametric fire [1]_.
    | 1 - Only to use travelling fire only.
    | 2 - Only to use Eurocode parametric fire, German Annex [2]_.
    | 3 - Use 0 and 1 as above based on certain conditions.
    | 4 - Use 2 and 1 as above based on certain conditions.

.. py:data:: n_simulations
    :type: int

    The number of simulations that will be running. A sensitivity analysis should be carried out to determine the
    appropriate number of simulations. This should be a positive integer greater or equal to one.

.. py:data:: room_breadth
    :type: float
    
    [:math:`m`] Breadth of room (the shorter dimension).

.. py:data:: 
    :type: float

    [:math:`m`] Depth of room (the greater dimension).

.. py:data:: room_height
    :type: float
    
    [:math:`m`] Height of room (floor slab to ceiling slab).

.. py:data:: room_wall_thermal_inertia
    :type: float
    
    [:math:`J/m²K√s`] Compartment lining thermal inertia. Thermal inertia is the tendency of a material to resist
    changes in temperature, i.e. to differentiate between thermal conductivity and heat capacity.

.. py:data:: window_width
    :type: float
    
    [:math:`m`] Total width of all opening areas for a compartment.

.. py:data:: window_height
    :type: float
    
    [:math:`m`] Weighted height of all opening areas.

.. py:data:: beam_position_vertical
    :type: float

    [:math:`m`] Height of test structure element within the compartment for TFM. This can be altered to assess the
    influence of height in tall compartments. Need to assess worst case height for columns.

.. py:data:: beam_position_horizontal
    :type: float

    [:math:`m`] Minimum beam location relative to compartment length for TFM - Linear distribution.

.. py:data:: window_open_fraction
    :type: float

    [:math:`1`].
    Glazing fall-out fraction.

.. py:data:: window_open_fraction_permanent
    :type: float

    [:math:`1`].
    Use this to force a ratio of open windows. If there is a vent to the outside this can be included here.

.. py:data:: fire_tlim
    :type: float

    [:math:`hour`] Time for maximum gas temperature in case of fuel-controlled fire, value options can be found in
    Annex A EN 1991-1-2 [1]_:

    | Slow: 25/60
    | Medium: 20/60
    | Fast: 15/60

.. py:data: fire_time_step
    :type: float

    [:math:`s`] Time step used for the model, all fire time-temperature curves and heat transfer calculation. This is
    recommended to be less than 30 s.

.. py:data:: fire_time_duration
    :type: float

    [:math:`s`] End of simulation. This should be set so that output data is produced allowing the target reliability
    to be determined. Normally set it to 4 hours and longer period of time for greater room length in order for
    travelling fire to propagate the entire room.

.. py:data:: fire_load_density
    :type: float

    [:math:`MJ/m²`] Fire load density. This should be selected based on occupancy characteristics. See literature for
    typical values for different occupancies [1]_ [3]_.

.. py:data:: fire_hrr_density
    :type: float

    [:math:`MW/m²`] Heat release rate. This should be selected based on the fuel. See literature for typical values for
    different occupancies [1]_ [3]_.

.. py:data:: fire_spread_speed
    :type: float

    [:math:`m/s`] Min spread rate for travelling fire.

.. py:data:: fire_nft_limit
    :type: float

    [:math:`K`] TFM near field temperature.

.. py:data:: fire_combustion_efficiency
    :type: float

    [:math:`1`].
    Combustion efficiency (0.8 to 1.0 [1]_ [3]_).

.. py:data:: fire_gamma_fi_q
    :type: float

    [:math:`1`].
    The partial factor for EC fire (German Annex).

.. py:data:: fire_t_alpha
    :type: float

    [:math:`s`] The fire growth factor.

.. py:data:: beam_cross_section_area
    :type: float

    [:math:`m²`] Cross sectional area of the section.

.. py:data:: beam_rho
    :type: float

    [:math:`kg/m³`] Density of the structural member.

.. py:data:: beam_temperature_goal
    :type: float

    [:math:`K`] Structural element (steel) failure temperature in Kelvin for goal seek.

.. py:data:: protection_protected_perimeter
    :type: float

    [:math:`m`] Heated perimeter.

.. py:data:: beam_protection_thickness
    :type: float

    [:math:`m`] Thickness of protection.

.. py:data:: protection_k
    :type: float

    [:math:`W/m/K`] Protection conductivity.

.. py:data:: protection_rho
    :type: float

    [:math:`kg/m³`] Density of protection to beam.

.. py:data:: protection_c
    :type: float

    [:math:`J/kg/K`] Specific heat of protection

.. py:data:: solver_temperature_goal
    :type: float

    [:math:`K`] The temperature to be solved for. This is critical temperature of the beam structural element, i.e. 550
    or 620 °C.

.. py:data:: solver_max_iter
    :type: float

    [:math:`1`].
    The maximum iteration for the solver to find convergence. Suggest 20 as most (if not all) cases converge in less
    than 20 iterations.

.. py:data:: solver_thickness_lbound
    :type: float

    [:math:`m`] The smallest value that the protection thickness can be. This is used to solve the maximum steel
    temperature at :py:data:`solver_temperature_goal`.

.. py:data:: solver_thickness_ubound
    :type: float

    [:math:`m`] The greatest value that the protection thickness can be. This is used to solve the maximum steel
    temperature at :py:data:`solver_temperature_goal`.

.. py:data:: solver_tol
    :type: float

    [:math:`K`] Tolerance of the temperature (in Kelvin) to be solved for. Set to 1 means convergence will be sought
    when the solved steel temperature is within :py:data:`solver_temperature_goal` :math:`\pm 1`.

.. py:data:: phi_teq
    :type: float

    [:math:`1`].
    Model uncertainty factor multiplied with the evaluated characteristic time equivalence value to get the design time
    equivalence value.

.. py:data:: timber_exposed_area
    :type: float

    [:math:`m²`] Exposed timber surface within the compartment, includes CLT slab, glulam columns and glulam beams.
    Set :py:data:`timber_exposed_area` to :math:`0` to omit timber involvement.

.. py:data:: timber_charring_rate
    :type: float

    [:math:`mm/min`] Timber constant charring rate. This is currently independent of temperature or heat flux.

.. py:data:: timber_hc
    :type: float

    [:math:`MJ/kg`] Heat of combustion of timber.

.. py:data:: timber_density
    :type: float

    [:math:`kg/m³`] Density of timber.

.. py:data:: timber_solver_ilim
    :type: float

    [:math:`1`].
    The maximum number of iterations that the solver can run. :py:data:`timber_solver_iter` in the output file should
    be inspected to determine appropriate value for `timber_solver_ilim`. Consider to increase
    :py:data:`timber_solver_ilim` (or increase :py:data:`timber_solver_tol`) if many solved values have
    :py:data:`timber_solver_iter` == `timber_solver_ilim`.

.. py:data:: timber_solver_tol
    :type: float

    [:math:`s`] Tolerance of the solver. Convergence is sought if change in time equivalence is less than
    :py:data:`timber_solver_tol`.


Output Files
============

MCS results are saved in :literal:`.\\mcs.out`, where :literal:`.\\` is the directory containing the input file.
Below shows an example directory tree including input and output files:

::

    .
    ├── input.xlsx
    └── mcs.out
        ├── case_a.csv
        ├── case_b.csv
        ├── case_c.csv
        ...

Where :literal:`.\\mcs.out\\case_name.csv` contain results of each simulation case (as per :py:data:`case_name`) and
this output file is produced upon completion of the simulation case. Below shows how an output file looks like.

.. math::

    \begin{matrix}
    \text{index}    & \text{beam_position_horizontal}   & \text{fire_combustion_efficiency}     & ... \\
    318             & 27.35                             & 0.96                                  & ... \\
    1065            & 25.04                             & 0.83                                  & ... \\
    1244            & 20.22                             & 0.92                                  & ... \\
    814             & 19.62                             & 0.94                                  & ... \\
    1276            & 18.75                             & 0.82                                  & ... \\
    ...             & ...                               & ...                                   & ...
    \end{matrix}

Following above, each row (except the first row) records the sampled stochastic inputs and simulation outputs for the
iteration

.. py:data:: index
    :type: int
    :noindex:

    An unique number associated with a MCS iteration.

.. py:data:: beam_position_horizontal
    :type: float
    :noindex:

    See :py:data:`beam_position_horizontal`.

.. py:data:: fire_combustion_efficiency
    :type: float

    See :py:data:`fire_combustion_efficiency`.

.. py:data:: fire_hrr_density
    :type: float
    :noindex:

    See :py:data:`fire_hrr_density`.

.. py:data:: fire_nft_limit
    :type: float
    :noindex:

    See :py:data:`fire_nft_limit`.

.. py:data:: fire_spread_speed
    :type: float
    :noindex:

    See :py:data:`fire_spread_speed`.


.. py:data:: window_open_fraction
    :type: float
    :noindex:

    See :py:data:`window_open_fraction`.

.. py:data:: fire_load_density
    :type: float
    :noindex:

    See :py:data:`fire_load_density` in inputs.

.. py:data:: fire_type
    :type: float

    The type of design fire being selected for the iteration. See :py:data:`fire_mode`.

    | 0: Parametric fire
    | 1: Travelling fire
    | 2: Parametric fire (DIN)

.. py:data:: extinction
    :type: float

    .. versionadded:: 0.1.3

    [:math:`s`] Fire extinction time.

    | For :py:data:`fire_type` 0 the extinction time is currently not determined.
    | For :py:data:`fire_type` 1 the extinction time is determined at the back face of the travelling fire reaching the end of the room.
    | For :py:data:`fire_type` 2 the extinction time is determined as the variable :math:`t_{3,x}` in J. Zehfuss and D. Hosser [4]_.

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

    The solved time equivalence value.

Reference
=========

.. [1]  BSI, *BS EN 1991-1-2:2002 Eurocode 1. Actions on structures. General actions. Actions on structures exposed to fire*, British Standards Institution, London, 2002.
.. [2]  DIN, *Eurocode 1: Actions on structures - Part 1-2: General actions - Actions on structures exposed to fire; German version EN 1991-1-2:2002 + AC:2009*. DIN Deutsches Institut für Normung e. V., Sep. 2015.
.. [3]  BSI, *PD 6688-1-2:2007 Background paper to the UK National Annex to BS EN 1991-1-2*, BSI, London, 2007.
.. [4]  J\. Zehfuss and D\. Hosser, *A parametric natural fire model for the structural fire design of multi-storey buildings*, Fire Safety Journal, vol. 42, no. 2, pp. 115–126, Mar. 2007.
