Flask React Services
====================

The `reflask` repository contains a simple flask blog application, with an API service.
The flask app provides for authoring posts, while React front end simply allows reading posts.

Architecture
------------

The architectural design has a number of principles which may seem unconventional at first.

  * Local CI/CD pipelines
  * Off line development
  * Develop over SSL
  * Environments on demand
  * Auto update of requirements
  * Local integration testing
  * Disposable builds

  > Note, not all of these are currently implemented in this repository.

 The rationale behind these principles is to maximise the efficiency of development, minimise
 technical debt, keep up to date with the rapidly evolving technological landscape, facilitate
 home working, reduce time to market, and fundamentally to deliver value and increase profitability.

 Structure
 ---------

 Follow the links below for documentation of the structural components.

   * [App](./app/README.md)
   * [Containers](./containers/README.md)
   * [Certificates](./keys/README.md)
   * [Requirements](./requirements/README.md)
