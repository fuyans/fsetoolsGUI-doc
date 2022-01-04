OFR Naming Convention
=====================

.. note::
    Documentation herein is based on the original official OFR Naming Convention email by Simon Lay in 2018.

Why do we need a file naming convention?

    We are a big team and we have some major projects with teams of engineers leading parallel delivery, we need some consistency to manage this from a QA perspective [LINK].
    Looking back and quickly identifying key project documents is much simpler when there is some rigour to the naming protocol.
    This level of rigour is expected for ISO 9001.

Why is it so complicated?

    Really, it isn’t complicated. It’s date, revision, project name and a plain English name, plus two optional fields (file type and security level).
    The “file type” and “security status” fields are deliberately at the end so that they can be left off if not considered relevant, but the preference is to use them.

Why reverse date?

    Because it neatly arranges files in order when looking by name.

Why not just use sequential revision numbers?

    For ISO 9001 we need to track revisions before they are issued.
    We need to differentiate between internal revisions and client comments.
    Won’t this mean saving a file loads of times? Yes, but you should be doing that already for QA!
    By defining that we start with 00 and move up from there and that we use Q for internal QA, D for external comments and R for formal revisions we just get some order to this.

Why use project number not name?

    Because project names change, numbers do not.
    Because project names are sometimes long, numbers are not.

What is “project stage”?

    This can be plain English or the RIBA stage or Works Package Stage or specific site within a portfolio.
    The key is that it should match the sub-project name that the work is being delivered under.
    Every project has sub-projects that you book time to, simply use the same one.

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

**Quality Assurance**

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
