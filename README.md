# Pyramid Slide Down (Maximum path sum II)

The repository contains solution for [Problem 67](https://projecteuler.net/problem=67) from [ProjectEuler](https://projecteuler.net).

The code also will be used to pass ["Pyramid Slide Down" Kata](https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python).

## Prerequisites

1. Make sure [Bazel](https://docs.bazel.build/versions/main/install.html) is installed on your environment:

    ```sh
    bazel version
    ```

2. Install package for virtual environment:

    ```sh
    pip install virtualenv
    ```

3. Create virtual environment:

    ```sh
    virtualenv venv
    ```

4. Activate virtual environment:

    ```sh
    # Posix
    source ./venv/bin/activate
    # DOS
    ./venv/scripts/activate.bat
    ```

5. Install all requirements:

    ```sh
    pip install -r requirements.txt
    ```

## Building

```sh
bazel build slide-down
```

## Testing

To run the suite:

```sh
pytest
```

To run the suite with coverage report:

```sh
pytest --cov=src
```

## Usage

There are three ways to use the code:

1. Run as console application with default behavior:

    ```sh
    bazel-bin/slide-down
    ```

    In this case all assets in JSON format at `./assets` directory will be processes. A user must be sure that valid JSON files (assets) present under `assets` directory.

2. Run as console application with custom asset(s):

    ```sh
    bazel-bin/slide-down my_pyramid.json
    ```

    Please refer `assets` directory of the project for valid JSON file examples.

3. Use core of the project as a part of another project:

    ```python
    from src.pyramid_slide_down import longest_slide_down
    pyramid = # ...
    longest_slide_down(pyramid)
    ```
