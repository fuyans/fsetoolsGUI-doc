BR 187 Parallel Oriented Emitter and Receiver
*********************************************

This module is capable of calculating the view factor for a parallel oriented emitter/receiver pair at any relative
locations:

1. When the receiver's normal projects at within the emitter.
2. When the receiver's normal projects on any edge of the emitter.
3. When the receiver's normal projects at any vertex of the emitter.
4. When the receiver's normal projects at outside of the emitter but directly above/below/above/beneath the emitter.
5. When the receiver's normal projects at outside of the emitter other than 4.

The calculation is based on the equation below (Equation A4, BR 187 [1]_) when receiver's normal projects at any vertex of the
emitter.

.. math::
    \phi = \frac{2}{\pi}\left(\frac{X}{A}\tan^{-1}{\left(\frac{Y}{A}\right)}+\frac{Y}{B}\tan^{-1}{\left(\frac{X}{B} \right )}\right)

where

    | :math:`A = \sqrt{1+X^2}`.
    | :math:`B = \sqrt{1+Y^2}`.
    | :math:`X = \frac{W}{2S}`.
    | :math:`Y = \frac{H}{2S}`.
    | :math:`W` is the emitter width, in [:math:`m`].
    | :math:`H` is the emitter height, in [:math:`m`].
    | :math:`S` is the separation distance between the emitter and receiver, in [:math:`m`].

.. [1] R. Chitty, *BR 187 External fire spread. Building separation and boundary distances.*, 2nd ed. Watford: BRE Bookshop, 2014.