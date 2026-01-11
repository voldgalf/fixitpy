Welcome to FixitPy's documentation!
===================================

**FixitPy** is a Python library for interfacing with iFixit's API interface.

.. container:: sd-badges-inline

    .. shield::
        :label: Github
        :message: FixitPy
        :color: darkcyan
        :logo: Github
        :link: https://github.com/voldgalf/FixitPy
        :link-type: url

    .. shield::
        :label: License
        :message: MIT
        :color: yellow

Installation
------------

.. code-block:: console

   (.venv) $ pip install FixitPy

Example Usage
------------

.. code-block:: python
    :linenos:

    import fixitpy

    guide = FixitPy.retrieve_guide(123)
    # 123 is an example and can be changed

    print(f"Title: {guide.get("title")}")
    print(f"Difficulty: {guide.get("difficulty")}")
    print(f"Conclusion: {guide.get("conclusion")}")

.. toctree::

    usage
    documentation
