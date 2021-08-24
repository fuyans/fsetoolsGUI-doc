OFR Naming convention
---------------------

.. list-table::
    :header-rows: 1

    * - Date
      - Author
      - Checker
      - Remarks
    * - 2020/03/30
      - Ian F.
      - Ian F.
      - Initial


.. list-table:: OFR Naming convention
    :widths: 3 7 90
    :header-rows: 1

    *
        - Order
        - Item
        - Description
    *
        - 1
        - **Date**
        -
            -  **YYMMDD**, in reverse number format, e.g. 180601.
            -  Ensures that when viewed in file management database the files sort in date order.
    *
        - 2
        - **Revision**
        -
            -  **Q##**, internal review drafts

                -  Q00, first issue for internal review.
                -  Q01, reviewer’s comments.
                -  Q02, authoriser’s comments.

            -  **D##**, draft issued outside for comments

                -  D00, first issue to others for comment.
                -  D01, Subsequent external reviews.

            -  **R##**, formal issue revision

                -  R00, first issue.
                -  R01, second issue.

            -  Reports should change formal issue revision when information that they are based upon changes. It is not the intent to use the Draft status to pick up design changes etc.
            -  At each revision change (including Q and D prefixes) the reason for change should be noted on the QA sheet and changes made using track changes with each version being saved to provide an audit trial.
    *
        - 3
        - **Project reference**
        -
            -  **OO#####**, replace OO with the originated office (i.e. LO for London, MA for Manchester etc.).
    *
        - 4
        - **Project stage**
        -
            -  Sub work packages or similar, e.g. WP1. It is recommended to use codes aligned to timesheet entry when possible.
    *
        - 5
        - **Title**
        -
            -  Plain English descriptor, e.g. “Outline_fire_safety_strategy”.
    *
        - 6
        - **Document type**
        -
            -  **GA**, general admin.
            -  **MD**, marketing documents.
            -  **FP**, fee proposal documents.
            -  **LT**, Letter.
            -  **DN**, design note.
            -  **OF**, outline strategy.
            -  **DF**, detailed strategy.
            -  **RF**, retrospective strategy.
            -  **FA**, fire risk assessment.
            -  **FS**, fire survey report.
            -  **FN**, file note.
            -  **MN**, meeting notes.
            -  **CS**, Calculation sheet.
            -  **SK**, sketch.
            -  **DW**, drawing.
            -  **XO**, expert opinion.
    *
        - 7
        - **Security status**
        -
            -  **CIC**, commercial in confidence.
            -  **WPC**, without prejudice and confidential.
            -  **SDS**, secure document.
            -  **FID**, free issue document (no security status).

.. math::
    :nowrap:

    \[
    \lambda =
    \left\{
    \begin{array}{
     @{}% no padding
     l@{\quad}% some padding
     r@{}% no padding
     >{{}}r@{}% no padding
     >{{}}l@{}% no padding
    }
    \frac{2}{3}h, &\text{no forced draught } \left[ False\right]\\
    \operatorname{min}\left({x, \frac{hx}{z}}\right)  &\text{forced draught }    \left[ True\right]\\
    \end{array}
    \right.
    \]
