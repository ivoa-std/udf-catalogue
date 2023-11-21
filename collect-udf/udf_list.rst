List of third party User Defined functions
******************************************

Generated with ``collect_adql_udf.py``

Last generated: 2023-11-21 14:19:13

``ARR_AVG(arr1 double[]) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Arithmetic mean of the array elements.

``ARR_COUNT(arr1 any[]) -> int``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the number of elements in the array.

``ARR_DOT(arr1 double[],arr2 double[]) -> double[]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Scalar product of two array. The scalar product of array of unequal length is NaN.

``ARR_IN(element any,arr1 any[]) -> boolean``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Test if an element is in the array.

``ARR_MAX(arr1 any[]) -> any``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Largest element in the array.

``ARR_MIN(arr1 any[]) -> any``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Smallest element in the array.

``ARR_SUM(arr1 double[]) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sum of all array elements.

``CEFCA_DMS_TO_DEGREES(value char) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Convert degrees, arcminute, arcsecond to a float degrees value.

``CEFCA_FLAMBDATOFNU(fnuflux double,filter int) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function converts a FLUX in 1e-19erg/(s.cm**2.Angstrom) to a FLUX in 1e-30erg/(s.cm**2.Hz).

``CEFCA_FNUFLUXTOJANSKY(flux double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function converts a FLUX in 1e-30 erg/s/cm2/Hz to a flux in Jansky.

``CEFCA_FNUFLUXTOMAGAB(flux double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function converts a FLUX in 1e-30 erg/s/cm2/Hz to a magnitude AB.  If flux is negative retrns -99 value.

``CEFCA_FNUTOFLAMBDA(fnuflux double,filter int) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function converts a FLUX in 1e-30erg/(s.cm**2.Hz) to a FLUX in 1e-19erg/(s.cm**2.Angstrom).

``CEFCA_HMS_TO_DEGREES(value char) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Convert hour, minute, second to a float degrees value.

``CEFCA_JANSKYTOFNUFLUX(fluxjansky double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function converts a flux in Jansky to a FLUX in 1e-30erg/(s.cm**2.Hz).

``CEFCA_MAGABTOFNUFLUX(magab double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function converts a magnitude AB to a FLUX in 1e-30erg/(s.cm**2.Hz).

``CEFCA_TS_TO_JD(ts char) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts a 'time.epoch' (timestamp) to a astronomical Julian Date.

``CEFCA_TS_TO_MJD(ts char) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts a 'time.epoch' (timestamp) to a astronomical Modified Julian date.

``ESO_DATEADD_SEC(seconds INTEGER, date TIMESTAMP) -> TIMESTAMP``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``ESO_INTERSECTION(region1 REGION, region2 REGION) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``ESO_SUBSTRING(string VARCHAR, start INTEGER, length INTEGER) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``GETDATE() -> TIMESTAMP``
^^^^^^^^^^^^^^^^^^^^^^^^^^

``IVO_BIT_AND_AGG(e int) -> int``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The bitwise AND of all non-null input values, or null if none.

``IVO_BIT_OR_AGG(e int) -> int``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The bitwise OR of all non-null input values, or null if none.

``IVO_CORR(x double,y double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Correlation coefficient.

``IVO_COVAR_SAMP(x double,y double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sample covariance.

``IVO_REGR_INTERCEPT(x double,y double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Y-intercept of the least-squares-fit linear equation determined by the (X, Y) pairs.

``IVO_REGR_R2(x double,y double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Square of the correlation coefficient.

``IVO_REGR_SLOPE(x double,y double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Slope of the least-squares-fit linear equation determined by the (X, Y) pairs.

``IVO_STDDEV(x double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sample standard deviation of the input values.

``IVO_STRING_AGG(e char,delimiter char) -> char``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Non-null input values concatenated into a string, separated by delimiter.

``IVO_VARIANCE(x double) -> double``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sample variance of the input values (square of the sample standard deviation).

``arr_avg(arr DOUBLE[]) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the average value of the array

``arr_max(arr DOUBLE[]) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the maximum value of the array

``arr_min(arr DOUBLE[]) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the min value of the array

``arr_sqrt(arr DOUBLE[]) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the square root of the array

``arr_stddev(arr DOUBLE[]) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the standard deviation of the array

``array_agg(str VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Aggregate inside an array the value of the given expression for each row.

``astrometric_parameter_error(e_ra_deg DOUBLE, e_de_deg DOUBLE, e_plx DOUBLE, e_pm_ra DOUBLE, e_pm_de DOUBLE, de_ra DOUBLE, plx_ra DOUBLE, plx_de DOUBLE, pm_ra_ra DOUBLE, pm_ra_de DOUBLE, pm_ra_plx DOUBLE, pm_de_ra DOUBLE, pm_de_de DOUBLE, pm_de_plx DOUBLE, pm_de_pm_ra DOUBLE, parallax DOUBLE, radial_velocity DOUBLE, e_rv DOUBLE) -> DOUBLE[21][1]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the astrometric parameter errors double array to be used as input for epoch_prop() function
						Parameters:
							e_ra_deg: Standard Error in Right Ascension (mas)
							e_de_deg: Standard Error in Declination (mas)
							e_plx: Standard Error in Parallax (mas)
							e_pm_ra: Standard Error in Proper Motion in RA (mas/yr)
							e_pm_de: Standard Error in Proper Motion in Dec (mas/yr)
							de_ra: Correlation Coefficient RA/Dec
							plx_ra: Correlation Coefficient Parallax/RA
							plx_de: Correlation Coefficient Parallax/Dec
							pm_ra_ra: Correlation Coefficient Proper Motion in RA/RA
							pm_ra_de: Correlation Coefficient Proper Motion in RA/Dec
							pm_ra_plx: Correlation Coefficient Proper Motion in RA/Parallax
							pm_de_ra: Correlation Coefficient Proper Motion in Dec/RA
							pm_de_de: Correlation Coefficient, Proper Motion in Dec/Dec
							pm_de_plx: Correlation Coefficient, Proper Motion in Dec/Parallax
							pm_de_pm_ra: Correlation Coefficient, Proper Motion in RA/Proper Motion in Dec
							parallax: Parallax (mas)
							radial_velocity: Radial Velocity (km/s)
							e_rv: Standard Error in Radial Velocity (km/s)

``astrometric_parameters(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE) -> DOUBLE[6][1]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the astrometric parameters double array to be used as input for epoch_prop() function
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)

``cbrt(x DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Cube Root
						Parameters:
							x: null

``cds_cast(expression DOUBLE, type VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(internal) cast numeric value to something

``cds_convert_epoch_prop_pos(ra DOUBLE, dec DOUBLE, systin VARCHAR, equinoxin REAL, epochin REAL, plx DOUBLE, pmra DOUBLE, pmdec DOUBLE, rv DOUBLE, systout VARCHAR, equinoxout REAL, epochout REAL) -> POINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Change  coordinate system ansd apply motion in position

``cds_convert_sys_pos(ra DOUBLE, dec DOUBLE, systin VARCHAR, equinoxin DOUBLE, systout VARCHAR, equinoxout DOUBLE) -> POINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Change of coordinate system

``cds_epoch_prop_pos(ra DOUBLE, dec DOUBLE, plx DOUBLE, pmra DOUBLE, pmdec DOUBLE, rv DOUBLE, epochin REAL, epochout REAL) -> POINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Apply motion on position

``cds_healpix_index(ra DOUBLE, dec DOUBLE) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
position to HEALPix in the indexed database order

``cds_lower(value VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
lower case function

``cds_round(value VARCHAR, nbdecimal INTEGER) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(internal)round numeric value (must be used with cds_cast)

``cds_upper(value VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
upper case function

``cot(x DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Cotangent of x
						Parameters:
							x: null

``div(y DOUBLE, x DOUBLE) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Integer quotient of y/x
						Parameters:
							y: null
							x: null

``epoch_prop(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE, astrometric_parameters VARBINARY) -> DOUBLE[6][1]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns all six input parameters (ra,dec,parallax,pm_ra,pm_dec,radial_velocity) propagated at the new arbitrary input epoch
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							ref_epoch: Reference Julian Epoch
							out_epoch: Final Julian Epoch
							astrometric_parameters: Array with the full six input parameters needed (ra[deg],dec[deg],plx[mas],pm_ra[mas/yr],pm_dec[mas/yr],pm_rv[mas/yr])

``epoch_prop_error(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, e_ra_deg DOUBLE, e_de_deg DOUBLE, e_plx DOUBLE, e_pm_ra DOUBLE, e_pm_de DOUBLE, e_rv DOUBLE, de_ra DOUBLE, plx_ra DOUBLE, plx_de DOUBLE, pm_ra_ra DOUBLE, pm_ra_de DOUBLE, pm_ra_plx DOUBLE, pm_de_ra DOUBLE, pm_de_de DOUBLE, pm_de_plx DOUBLE, pm_de_pm_ra DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE, astrometric_parameters VARBINARY, astrometric_parameter_error VARBINARY) -> DOUBLE[21][1]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the error vector with the uncertainties associated to the propagated astrometric parameters plus the set of propagated correlation parameters
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							e_ra_deg: Standard Error in Right Ascension (mas)
							e_de_deg: Standard Error in Declination (mas)
							e_plx: Standard Error in Parallax (mas)
							e_pm_ra: Standard Error in Proper Motion in RA (mas/yr)
							e_pm_de: Standard Error in Proper Motion in Dec (mas/yr)
							e_rv: Standard Error in Radial Velocity (km/s)
							de_ra: Correlation Coefficient RA/Dec
							plx_ra: Correlation Coefficient Parallax/RA
							plx_de: Correlation Coefficient Parallax/Dec
							pm_ra_ra: Correlation Coefficient Proper Motion in RA/RA
							pm_ra_de: Correlation Coefficient Proper Motion in RA/Dec
							pm_ra_plx: Correlation Coefficient Proper Motion in RA/Parallax
							pm_de_ra: Correlation Coefficient Proper Motion in Dec/RA
							pm_de_de: Correlation Coefficient, Proper Motion in Dec/Dec
							pm_de_plx: Correlation Coefficient, Proper Motion in Dec/Parallax
							pm_de_pm_ra: Correlation Coefficient, Proper Motion in RA/Proper Motion in Dec
							ref_epoch: Reference Julian Epoch (yr)
							out_epoch: Final Julian Epoch (yr)
							astrometric_parameters: Array with the full six input parameters needed (ra[deg],dec[deg],plx[mas],pm_ra[mas/yr],pm_dec[mas/yr],pm_rv[mas/yr])
							astrometric_parameter_error: Array with the 21 covariance matrix elements (output from astrometric_parameter_error ADQL function)

``epoch_prop_pos(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE) ->``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the new position (ra,dec) of the source at the new arbitrary input epoch
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							ref_epoch: Reference Julian Epoch
							out_epoch: Final Julian Epoch

``esdc_array_dims(n VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns a text representation of array dimensions
						Parameters:
							n: Input array.

``esdc_array_element(n VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns an array representation of input values
						Parameters:
							n: Input array elements.

``esdc_array_length(n VARCHAR, dim INTEGER) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the length of the requested array dimension
						Parameters:
							n: Input array.
							dim: Input dimension.

``esdc_array_ndims(n VARCHAR) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the number of dimensions of the array.
						Parameters:
							n: Input array.

``esdc_astrometric_parameter_error(e_ra_deg DOUBLE, e_de_deg DOUBLE, e_plx DOUBLE, e_pm_ra DOUBLE, e_pm_de DOUBLE, de_ra DOUBLE, plx_ra DOUBLE, plx_de DOUBLE, pm_ra_ra DOUBLE, pm_ra_de DOUBLE, pm_ra_plx DOUBLE, pm_de_ra DOUBLE, pm_de_de DOUBLE, pm_de_plx DOUBLE, pm_de_pm_ra DOUBLE, parallax DOUBLE, radial_velocity DOUBLE, e_rv DOUBLE) -> DOUBLE[21]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the astrometric parameter errors double array to be used as input for epoch_prop() function
						Parameters:
							e_ra_deg: Standard Error in Right Ascension (mas)
							e_de_deg: Standard Error in Declination (mas)
							e_plx: Standard Error in Parallax (mas)
							e_pm_ra: Standard Error in Proper Motion in RA (mas/yr)
							e_pm_de: Standard Error in Proper Motion in Dec (mas/yr)
							de_ra: Correlation Coefficient RA/Dec
							plx_ra: Correlation Coefficient Parallax/RA
							plx_de: Correlation Coefficient Parallax/Dec
							pm_ra_ra: Correlation Coefficient Proper Motion in RA/RA
							pm_ra_de: Correlation Coefficient Proper Motion in RA/Dec
							pm_ra_plx: Correlation Coefficient Proper Motion in RA/Parallax
							pm_de_ra: Correlation Coefficient Proper Motion in Dec/RA
							pm_de_de: Correlation Coefficient, Proper Motion in Dec/Dec
							pm_de_plx: Correlation Coefficient, Proper Motion in Dec/Parallax
							pm_de_pm_ra: Correlation Coefficient, Proper Motion in RA/Proper Motion in Dec
							parallax: Parallax (mas)
							radial_velocity: Radial Velocity (km/s)
							e_rv: Standard Error in Radial Velocity (km/s)

``esdc_astrometric_parameter_error(e_ra_deg DOUBLE, e_de_deg DOUBLE, e_plx DOUBLE, e_pm_ra DOUBLE, e_pm_de DOUBLE, de_ra DOUBLE, plx_ra DOUBLE, plx_de DOUBLE, pm_ra_ra DOUBLE, pm_ra_de DOUBLE, pm_ra_plx DOUBLE, pm_de_ra DOUBLE, pm_de_de DOUBLE, pm_de_plx DOUBLE, pm_de_pm_ra DOUBLE, parallax DOUBLE, radial_velocity DOUBLE, e_rv DOUBLE) -> DOUBLE[21][1]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the astrometric parameter errors double array to be used as input for epoch_prop() function
						Parameters:
							e_ra_deg: Standard Error in Right Ascension (mas)
							e_de_deg: Standard Error in Declination (mas)
							e_plx: Standard Error in Parallax (mas)
							e_pm_ra: Standard Error in Proper Motion in RA (mas/yr)
							e_pm_de: Standard Error in Proper Motion in Dec (mas/yr)
							de_ra: Correlation Coefficient RA/Dec
							plx_ra: Correlation Coefficient Parallax/RA
							plx_de: Correlation Coefficient Parallax/Dec
							pm_ra_ra: Correlation Coefficient Proper Motion in RA/RA
							pm_ra_de: Correlation Coefficient Proper Motion in RA/Dec
							pm_ra_plx: Correlation Coefficient Proper Motion in RA/Parallax
							pm_de_ra: Correlation Coefficient Proper Motion in Dec/RA
							pm_de_de: Correlation Coefficient, Proper Motion in Dec/Dec
							pm_de_plx: Correlation Coefficient, Proper Motion in Dec/Parallax
							pm_de_pm_ra: Correlation Coefficient, Proper Motion in RA/Proper Motion in Dec
							parallax: Parallax (mas)
							radial_velocity: Radial Velocity (km/s)
							e_rv: Standard Error in Radial Velocity (km/s)

``esdc_astrometric_parameter_error(e_ra_deg DOUBLE, e_de_deg DOUBLE, e_plx DOUBLE, e_pm_ra DOUBLE, e_pm_de DOUBLE, de_ra DOUBLE, plx_ra DOUBLE, pm_ra_ra DOUBLE, pm_de_ra DOUBLE, plx_de DOUBLE, pm_ra_de DOUBLE, pm_de_de DOUBLE, pm_ra_plx DOUBLE, pm_de_plx DOUBLE, pm_de_pm_ra DOUBLE, parallax DOUBLE, radial_velocity DOUBLE, e_rv DOUBLE) -> DOUBLE[21]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the astrometric parameter errors double array to be used as input for epoch_prop() function
						Parameters:
							e_ra_deg: Standard Error in Right Ascension (mas)
							e_de_deg: Standard Error in Declination (mas)
							e_plx: Standard Error in Parallax (mas)
							e_pm_ra: Standard Error in Proper Motion in RA (mas/yr)
							e_pm_de: Standard Error in Proper Motion in Dec (mas/yr)
							de_ra: Correlation Coefficient RA/Dec
							plx_ra: Correlation Coefficient Parallax/RA
							pm_ra_ra: Correlation Coefficient Proper Motion in RA/RA
							pm_de_ra: Correlation Coefficient Proper Motion in Dec/RA
							plx_de: Correlation Coefficient Parallax/Dec
							pm_ra_de: Correlation Coefficient Proper Motion in RA/Dec
							pm_de_de: Correlation Coefficient, Proper Motion in Dec/Dec
							pm_ra_plx: Correlation Coefficient Proper Motion in RA/Parallax
							pm_de_plx: Correlation Coefficient, Proper Motion in Dec/Parallax
							pm_de_pm_ra: Correlation Coefficient, Proper Motion in RA/Proper Motion in Dec
							parallax: Parallax (mas)
							radial_velocity: Radial Velocity (km/s)
							e_rv: Standard Error in Radial Velocity (km/s)

``esdc_astrometric_parameters(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE) -> DOUBLE[6]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the astrometric parameters double array to be used as input for epoch_prop() function
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)

``esdc_astrometric_parameters(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE) -> DOUBLE[6][1]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the astrometric parameters double array to be used as input for epoch_prop() function
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)

``esdc_cardinality(n VARCHAR) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the total number of elements in the array, or 0 if the array is empty.
						Parameters:
							n: Input array.

``esdc_case_condition(default_value VARCHAR, conditions VARCHAR, results VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For an array of input conditions and results, return the first one found true.
						Parameters:
							default_value: Value to return if all conditions are false.
							conditions: Input conditions array.
							results: Input results array.

``esdc_case_expression(input_value VARCHAR, default_value VARCHAR, condition_values VARCHAR, results VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For an array of input conditions and results, return the first one found equal to input value.
						Parameters:
							input_value: Value to compare condition values with.
							default_value: Value to return if none of condition_values equal input_value.
							condition_values: Input results array.
							results: Input results array.

``esdc_coalesce(n VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the first of its arguments that is not null
						Parameters:
							n: Nth input element.

``esdc_crossmatch_positional(table_schema_a VARCHAR, table_name_a VARCHAR, table_schema_b VARCHAR, table_name_b VARCHAR, radius DOUBLE, output_table_schema VARCHAR, output_table_name VARCHAR) -> BIGINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For input tables, create a positional crossmatch for input radius and store it in a separate table.
						Parameters:
							table_schema_a: First table schema.
							table_name_a: First table name.
							table_schema_b: Second table schema.
							table_name_b: Second table name.
							radius: Crossmatch radius.
							output_table_schema: Output table schema.
							output_table_name: Output table name.

``esdc_epoch_prop(astrometric_parameters DOUBLE[6], ref_epoch DOUBLE, out_epoch DOUBLE) -> DOUBLE[6]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns all six input parameters (ra,de,parallax,pm_ra,pm_de,radial_velocity) propagated from the reference epoch to an arbitrary epoch.
						Parameters:
							astrometric_parameters: Array with the full six input parameters needed (ra[deg],dec[deg],plx[mas],pm_ra[mas/yr],pm_dec[mas/yr],pm_rv[mas/yr])
							ref_epoch: Reference Julian Epoch
							out_epoch: Final Julian Epoch

``esdc_epoch_prop(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE) -> DOUBLE[6]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns all six input parameters (ra,de,parallax,pm_ra,pm_de,radial_velocity) propagated from the reference epoch to an arbitrary epoch.
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							ref_epoch: Reference Julian Epoch
							out_epoch: Final Julian Epoch

``esdc_epoch_prop(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE, astrometric_parameters VARBINARY) -> DOUBLE[6]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns all six input parameters (ra,dec,parallax,pm_ra,pm_dec,radial_velocity) propagated at the new arbitrary input epoch
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							ref_epoch: Reference Julian Epoch
							out_epoch: Final Julian Epoch
							astrometric_parameters: Array with the full six input parameters needed (ra[deg],dec[deg],plx[mas],pm_ra[mas/yr],pm_dec[mas/yr],pm_rv[mas/yr])

``esdc_epoch_prop(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE, astrometric_parameters VARBINARY) -> DOUBLE[6][1]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns all six input parameters (ra,dec,parallax,pm_ra,pm_dec,radial_velocity) propagated at the new arbitrary input epoch
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							ref_epoch: Reference Julian Epoch
							out_epoch: Final Julian Epoch
							astrometric_parameters: Array with the full six input parameters needed (ra[deg],dec[deg],plx[mas],pm_ra[mas/yr],pm_dec[mas/yr],pm_rv[mas/yr])

``esdc_epoch_prop_covariance(ra DOUBLE, dec DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, e_ra_deg DOUBLE, e_de_deg DOUBLE, e_plx DOUBLE, e_pm_ra DOUBLE, e_pm_de DOUBLE, e_rv DOUBLE, de_ra DOUBLE, plx_ra DOUBLE, plx_de DOUBLE, pm_ra_ra DOUBLE, pm_ra_de DOUBLE, pm_ra_plx DOUBLE, pm_de_ra DOUBLE, pm_de_de DOUBLE, pm_de_plx DOUBLE, pm_de_pm_ra DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE) -> DOUBLE[6][6]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the propagated covariance matrix from the epoch_prop function
						Parameters:
							ra: Right Ascension (deg)
							dec: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							e_ra_deg: Standard Error in Right Ascension (mas)
							e_de_deg: Standard Error in Declination (mas)
							e_plx: Standard Error in Parallax (mas)
							e_pm_ra: Standard Error in Proper Motion in RA (mas/yr)
							e_pm_de: Standard Error in Proper Motion in Dec (mas/yr)
							e_rv: Standard Error in Radial Velocity (km/s)
							de_ra: Correlation Coefficient RA/Dec
							plx_ra: Correlation Coefficient Parallax/RA
							plx_de: Correlation Coefficient Parallax/Dec
							pm_ra_ra: Correlation Coefficient Proper Motion in RA/RA
							pm_ra_de: Correlation Coefficient Proper Motion in RA/Dec
							pm_ra_plx: Correlation Coefficient Proper Motion in RA/Parallax
							pm_de_ra: Correlation Coefficient Proper Motion in Dec/RA
							pm_de_de: Correlation Coefficient, Proper Motion in Dec/Dec
							pm_de_plx: Correlation Coefficient, Proper Motion in Dec/Parallax
							pm_de_pm_ra: Correlation Coefficient, Proper Motion in RA/Proper Motion in Dec
							ref_epoch: Reference Julian Epoch (yr)
							out_epoch: Final Julian Epoch (yr)

``esdc_epoch_prop_error(astrometric_parameters DOUBLE[6], astrometric_parameter_error DOUBLE[21], ref_epoch DOUBLE, out_epoch DOUBLE) -> DOUBLE[21]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the error vector with the uncertainties associated to the propagated astrometric parameters plus the set of propagated correlation parameters
						Parameters:
							astrometric_parameters: Array with the full six input parameters needed (ra[deg],dec[deg],plx[mas],pm_ra[mas/yr],pm_dec[mas/yr],pm_rv[mas/yr])
							astrometric_parameter_error: Array with the 21 covariance matrix elements (output from astrometric_parameter_error ADQL function)
							ref_epoch: Reference Julian Epoch
							out_epoch: Final Julian Epoch

``esdc_epoch_prop_error(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, e_ra_deg DOUBLE, e_de_deg DOUBLE, e_plx DOUBLE, e_pm_ra DOUBLE, e_pm_de DOUBLE, e_rv DOUBLE, de_ra DOUBLE, plx_ra DOUBLE, plx_de DOUBLE, pm_ra_ra DOUBLE, pm_ra_de DOUBLE, pm_ra_plx DOUBLE, pm_de_ra DOUBLE, pm_de_de DOUBLE, pm_de_plx DOUBLE, pm_de_pm_ra DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE, astrometric_parameters VARBINARY, astrometric_parameter_error VARBINARY) -> DOUBLE[21]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the error vector with the uncertainties associated to the propagated astrometric parameters plus the set of propagated correlation parameters
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							e_ra_deg: Standard Error in Right Ascension (mas)
							e_de_deg: Standard Error in Declination (mas)
							e_plx: Standard Error in Parallax (mas)
							e_pm_ra: Standard Error in Proper Motion in RA (mas/yr)
							e_pm_de: Standard Error in Proper Motion in Dec (mas/yr)
							e_rv: Standard Error in Radial Velocity (km/s)
							de_ra: Correlation Coefficient RA/Dec
							plx_ra: Correlation Coefficient Parallax/RA
							plx_de: Correlation Coefficient Parallax/Dec
							pm_ra_ra: Correlation Coefficient Proper Motion in RA/RA
							pm_ra_de: Correlation Coefficient Proper Motion in RA/Dec
							pm_ra_plx: Correlation Coefficient Proper Motion in RA/Parallax
							pm_de_ra: Correlation Coefficient Proper Motion in Dec/RA
							pm_de_de: Correlation Coefficient, Proper Motion in Dec/Dec
							pm_de_plx: Correlation Coefficient, Proper Motion in Dec/Parallax
							pm_de_pm_ra: Correlation Coefficient, Proper Motion in RA/Proper Motion in Dec
							ref_epoch: Reference Julian Epoch (yr)
							out_epoch: Final Julian Epoch (yr)
							astrometric_parameters: Array with the full six input parameters needed (ra[deg],dec[deg],plx[mas],pm_ra[mas/yr],pm_dec[mas/yr],pm_rv[mas/yr])
							astrometric_parameter_error: Array with the 21 covariance matrix elements (output from astrometric_parameter_error ADQL function)

``esdc_epoch_prop_error(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, e_ra_deg DOUBLE, e_de_deg DOUBLE, e_plx DOUBLE, e_pm_ra DOUBLE, e_pm_de DOUBLE, e_rv DOUBLE, de_ra DOUBLE, plx_ra DOUBLE, plx_de DOUBLE, pm_ra_ra DOUBLE, pm_ra_de DOUBLE, pm_ra_plx DOUBLE, pm_de_ra DOUBLE, pm_de_de DOUBLE, pm_de_plx DOUBLE, pm_de_pm_ra DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE, astrometric_parameters VARBINARY, astrometric_parameter_error VARBINARY) -> DOUBLE[21][1]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the error vector with the uncertainties associated to the propagated astrometric parameters plus the set of propagated correlation parameters
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							e_ra_deg: Standard Error in Right Ascension (mas)
							e_de_deg: Standard Error in Declination (mas)
							e_plx: Standard Error in Parallax (mas)
							e_pm_ra: Standard Error in Proper Motion in RA (mas/yr)
							e_pm_de: Standard Error in Proper Motion in Dec (mas/yr)
							e_rv: Standard Error in Radial Velocity (km/s)
							de_ra: Correlation Coefficient RA/Dec
							plx_ra: Correlation Coefficient Parallax/RA
							plx_de: Correlation Coefficient Parallax/Dec
							pm_ra_ra: Correlation Coefficient Proper Motion in RA/RA
							pm_ra_de: Correlation Coefficient Proper Motion in RA/Dec
							pm_ra_plx: Correlation Coefficient Proper Motion in RA/Parallax
							pm_de_ra: Correlation Coefficient Proper Motion in Dec/RA
							pm_de_de: Correlation Coefficient, Proper Motion in Dec/Dec
							pm_de_plx: Correlation Coefficient, Proper Motion in Dec/Parallax
							pm_de_pm_ra: Correlation Coefficient, Proper Motion in RA/Proper Motion in Dec
							ref_epoch: Reference Julian Epoch (yr)
							out_epoch: Final Julian Epoch (yr)
							astrometric_parameters: Array with the full six input parameters needed (ra[deg],dec[deg],plx[mas],pm_ra[mas/yr],pm_dec[mas/yr],pm_rv[mas/yr])
							astrometric_parameter_error: Array with the 21 covariance matrix elements (output from astrometric_parameter_error ADQL function)

``esdc_epoch_prop_error(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, e_ra_deg DOUBLE, e_de_deg DOUBLE, e_plx DOUBLE, e_pm_ra DOUBLE, e_pm_de DOUBLE, e_rv DOUBLE, de_ra DOUBLE, plx_ra DOUBLE, pm_ra_ra DOUBLE, pm_de_ra DOUBLE, plx_de DOUBLE, pm_ra_de DOUBLE, pm_de_de DOUBLE, pm_ra_plx DOUBLE, pm_de_plx DOUBLE, pm_de_pm_ra DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE) -> DOUBLE[21]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the error vector with the uncertainties associated to the propagated astrometric parameters plus the set of propagated correlation parameters
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							e_ra_deg: Standard Error in Right Ascension (mas)
							e_de_deg: Standard Error in Declination (mas)
							e_plx: Standard Error in Parallax (mas)
							e_pm_ra: Standard Error in Proper Motion in RA (mas/yr)
							e_pm_de: Standard Error in Proper Motion in Dec (mas/yr)
							e_rv: Standard Error in Radial Velocity (km/s)
							de_ra: Correlation Coefficient RA/Dec
							plx_ra: Correlation Coefficient Parallax/RA
							pm_ra_ra: Correlation Coefficient Proper Motion in RA/RA
							pm_de_ra: Correlation Coefficient Proper Motion in Dec/RA
							plx_de: Correlation Coefficient Parallax/Dec
							pm_ra_de: Correlation Coefficient Proper Motion in RA/Dec
							pm_de_de: Correlation Coefficient, Proper Motion in Dec/Dec
							pm_ra_plx: Correlation Coefficient Proper Motion in RA/Parallax
							pm_de_plx: Correlation Coefficient, Proper Motion in Dec/Parallax
							pm_de_pm_ra: Correlation Coefficient, Proper Motion in RA/Proper Motion in Dec
							ref_epoch: Reference Julian Epoch (yr)
							out_epoch: Final Julian Epoch (yr)

``esdc_epoch_prop_pos(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE) ->``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the new position (ra,dec) of the source at the new arbitrary input epoch
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							ref_epoch: Reference Julian Epoch
							out_epoch: Final Julian Epoch

``esdc_epoch_prop_pos(ra DOUBLE, de DOUBLE, parallax DOUBLE, pm_ra DOUBLE, pm_de DOUBLE, radial_velocity DOUBLE, ref_epoch DOUBLE, out_epoch DOUBLE) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the new position (ra,dec) of the source at the new arbitrary input epoch
						Parameters:
							ra: Right Ascension (deg)
							de: Declination (deg)
							parallax: Parallax (mas)
							pm_ra: Proper Motion in Right Ascension (mas/yr)
							pm_de: Proper Motion in Declination (mas/yr)
							radial_velocity: Radial Velocity (km/s)
							ref_epoch: Reference Julian Epoch
							out_epoch: Final Julian Epoch

``esdc_greatest(v1 DOUBLE, v2 DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Select the largest value among given arguments.
						Parameters:
							v1: First argument.
							v2: Second argument.

``esdc_if_then_else(condition VARCHAR, ouput_value VARCHAR, default_value VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If input condition is true, return output value. Otherwise return default value.
						Parameters:
							condition: Value to compare to true.
							ouput_value: Value to return if condition is true.
							default_value: Value to return if condition is false.

``esdc_least(v1 DOUBLE, v2 DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Select the smallest value among given arguments.
						Parameters:
							v1: First argument.
							v2: Second argument.

``esdc_left(string VARCHAR, n INTEGER) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function returns the first n characters in the string.
						Parameters:
							string: a string from which a number of the leftmost characters is returned.
							n: an integer that specifies the number of left-most characters in the string should be returned. If n is negative, the function returns the leftmost characters in the string but last |n| (absolute) characters.

``esdc_length(string VARCHAR) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function returns the number of characters in the string.
						Parameters:
							string: the string that you want to calculate its length.

``esdc_nullif(value1 VARCHAR, value2 VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns a null value if value1 equals value2; otherwise it returns value1.
						Parameters:
							value1: Input value 1.
							value2: Input value 2.

``esdc_position(substring VARCHAR, string VARCHAR) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function returns the location of a substring in a string.
						Parameters:
							substring: the string that you want to locate.
							string: the string for which the substring is searched.

``esdc_radial_velocity(parallax DOUBLE, pm_rv DOUBLE) ->``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the radial velocity in units of mas/yr
						Parameters:
							parallax: Parallax (mas)
							pm_rv: Radial proper motion (mas/yr)

``esdc_radial_velocity(pm_rv DOUBLE, parallax DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the radial velocity in units of mas/yr
						Parameters:
							pm_rv: Radial proper motion (mas/yr)
							parallax: Parallax (mas)

``esdc_right(string VARCHAR, n INTEGER) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function returns the last n characters in a string.
						Parameters:
							string: a string from which a number of the rightmost characters is returned.
							n: an integer that specifies the number of right-most characters in the string should be returned. If n is negative, the function returns all characters in the string but first |n| (absolute) characters.

``esdc_stddev(n DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Standard deviation.
						Parameters:
							n: Input value.

``esdc_substring(string VARCHAR, start_position INTEGER, length INTEGER) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function returns a part of string.
						Parameters:
							string: the string that you want to get a part extracted.
							start_position: an integer that specifies where you want to extract the substring. If start_position equals zero, the substring starts at the first character of the string. The start_position can be only positive
							length: a positive integer that determines the number of characters that you want to extract from the string beginning at start_position. If the sum of start_position and length is greater than the number of characters in the string, the substring function returns the whole string beginning at start_position. The length parameter is optional. If you omit the length parameter, the substring function returns the whole string started at start_position.

``esdc_to_bigint(n DOUBLE) -> BIGINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts input value to BIGINT type.
						Parameters:
							n: Input value.

``esdc_to_boolean(n INTEGER) -> BOOLEAN``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts input value to BOOLEAN type.
						Parameters:
							n: Input value.

``esdc_to_char(n DOUBLE) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts input value to VARCHAR type.
						Parameters:
							n: Input value.

``esdc_to_double(n DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts input value to DOUBLE type.
						Parameters:
							n: Input value.

``esdc_to_integer(n DOUBLE) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts input value to INTEGER type.
						Parameters:
							n: Input value.

``esdc_to_real(n DOUBLE) -> REAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts input value to REAL type.
						Parameters:
							n: Input value.

``esdc_to_smallint(n DOUBLE) -> SMALLINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts input value to SMALLINT type.
						Parameters:
							n: Input value.

``esdc_translate(string VARCHAR, from VARCHAR, to VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function performs several single-character, one-to-one translation in one operation.
						Parameters:
							string: the string subjected to translation.
							from: a set of characters in the first argument (_string_) that should be replaced.
							to: a set of characters that replaces the _from_ in the _string_.

``esdc_trim(characters VARCHAR, string VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
removes the longest string that contains a specific character from a string. By default, the function removes spaces if you don’t specify explicitly which character you want to remove.
						Parameters:
							characters: optional parameter that defines a literal specifying explicitly which characters you want to remove in the string. Accepted literals are: LEADING, TRAILING and BOTH. Example of use: TRIM(BOTH, string)
							string: the string for which the removal is requested. Mandatory parameter: example of use: TRIM(string)

``gaia_healpix_index(hpxOrder INTEGER, sourceId BIGINT) -> BIGINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the index of the (nest) Healpix cell (at the specified order: hpxOrder) containing the specified Gaia source. The Healpix index is actually extracted from the given Gaia source_id.

``gaia_healpix_index(norder INTEGER, gaia_source_id BIGINT) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the healpix index of the given norder extracted from the given gaia Source ID
						Parameters:
							norder: null
							gaia_source_id: null

``gavo_apply_pm(ra DOUBLE PRECISION, dec DOUBLE PRECISION, pmra DOUBLE PRECISION, pmde DOUBLE PRECISION, epdist DOUBLE PRECISION) -> POINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns a POINT (in the UNDEFINED reference frame) for the position
an object at ra/dec with proper motion pmra/pmde has after epdist years.

positions must be in degrees, PMs in should be in julian years (i.e., proper
motions are expected in degrees/year).  pmra is assumed to contain 
cos(delta).

This function goes through the tangential plane.  Since it does not have
information on distance and radial velocity, it cannot reconstruct
the true space motion, and hence its results will degrade over time.

This function should not be used in new queries; use gavo_epoch_prop
instead.

``gavo_getauthority(ivoid TEXT) -> TEXT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
returns the authority part of an ivoid (or, more generally a URI).
So, ivo://org.gavo.dc/foo/bar#baz becomes org.gavo.dc.

The behaviour for anything that's not a full URI is undefined.

``gavo_histogram(val REAL) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This aggregate function returns a histogram of val with nbins+2 elements.
						Parameters:
							val: the value to bin.

``gavo_histogram(val REAL, lower REAL, upper REAL, nbins INTEGER) -> INTEGER[*]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This aggregate function returns a histogram of val with nbins+2 elements. Assuming 0-based arrays, results[0] contains the number of underflows (i.e., val < lower), result[nbins+1] the number of overflows. Elements 1…nbins are the counts in nbins bins of width (upper−lower)/nbins. Clients will have to convert back to physical units using some external communication, as there currently is no (meta-) data as lower and upper in the TAP response.
						Parameters:
							val: the value to bin.
							lower: the lower limit of the histogram
							upper: the upper limit of the histogram
							nbins: the number of "natural" bins in the histogram.

``gavo_histogram(val REAL, lower REAL, upper REAL, nbins INTEGER) -> INTEGER[]``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The aggregate function returns a histogram of val with nbins+2 elements.
Assuming 0-based arrays, result[0] contains the number of underflows (i.e.,
val<lower), result[nbins+1] the number of overflows.  Elements 1..nbins
are the counts in nbins bins of width (upper-lower)/nbins.  Clients
will have to convert back to physical units using some external 
communication, there currently is no (meta-) data as lower and upper in
the TAP response.

``gavo_ipix(long REAL, lat REAL) -> BIGINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gavo_ipix returns the q3c ipix for a long/lat pair (it simply wraps
the 13c_ang2ipix function).

This is probably only relevant when you play tricks with indices or
PPMXL ids.

``gavo_match(pattern TEXT, string TEXT) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gavo_match returns 1 if the POSIX regular expression pattern
matches anything in string, 0 otherwise.

``gavo_mocintersect(moc1 MOC, moc2 MOC) -> MOC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
returns the intersection of two MOCs.

``gavo_mocunion(moc1 MOC, moc2 MOC) -> MOC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
returns the union of two MOCs.

``gavo_normal_random(mu REAL, sigma REAL) -> REAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function returns a random number drawn from a normal distribution
with mean mu and width sigma.

Implementation note: Right now, the Gaussian is approximated by
summing up and scaling ten calls to random.  This, hence, is not
very precise or fast.  It might work for some use cases, and we
will provide a better implementation if this proves inadequate.

``gavo_simbadpoint(identifier TEXT) -> POINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gavo_simbadpoint queries simbad for an identifier and returns the 
corresponding point.  Note that identifier can only be a literal,
i.e., as simple string rather than a column name. This is because
our database cannot query simbad, and we probably wouldn't want
to fire off millions of simbad queries anyway; use simbad's own
TAP service for this kind of application.

``gavo_simbadpoint(identifier VARCHAR) -> POINT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Queries Simbad for an identifier and returns the corresponding point.
						Parameters:
							identifier: A string containing an identifier Simbad can resolve.

``gavo_simbadpoint(identifier VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Queries Simbad for an identifier and returns the corresponding point.
						Parameters:
							identifier: A string containing an identifier Simbad can resolve.

``gavo_specconv(expr DOUBLE PRECISION, dest_unit TEXT) -> DOUBLE PRECISION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
returns the spectral value expr converted to dest_unit.

expr has to be in either energy, wavelength, or frequency, and dest_unit
must be a VOUnit giving another spectral unit (e.g., MHz, keV, nm, or
Angstrom). This is intended to let users express spectral constraints
in their preferred unit independently of the choice of unit in the 
database.  Examples::

	gavo_specconv(obscore.em_min, "keV") > 300
	gavo_specconv(obscore.em_max, "MHz") > 30
	gavo_specconv(spectral_start, "Angstrom") > 4000

There is a variant of gavo_specconv accepting expr's unit in a third
argument.

``gavo_specconv(expr NUMERIC, expr_unit TEXT dest_unit TEXT) -> NUMERIC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
returns expr assumed to be in expr_unit expressed in dest_unit.

		This is a variant of the two-argument gavo_specconv for when
		the unit of expr is not known to the ADQL translator, either because
		it because it is a literal or because it does not look like
		a spectral unit.  Examples::

			gavo_specconv(656, 'nm', 'J') BETWEEN spectral_start AND spectral_end
			gavo_specconv(arccos(phi)*incidence, 'Hz', 'eV')
		
		Clearly, overriding known units is likely to yield bad results;
		the translator therefore warns if an existing unit is overridden
		with a different unit.

``gavo_specconv(expr NUMERIC, expr_unit TEXT, dest_unit TEXT) -> NUMERIC``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
returns expr assumed to be in expr_unit expressed in dest_unit.

		This is a variant of the two-argument gavo_specconv for when
		the unit of expr is not known to the ADQL translator, either because
		it because it is a literal or because it does not look like
		a spectral unit.  Examples::

			gavo_specconv(656, 'nm', 'J') BETWEEN spectral_start AND spectral_end
			gavo_specconv(arccos(phi)*incidence, 'Hz', 'eV')
		
		Clearly, overriding known units is likely to yield bad results;
		the translator therefore warns if an existing unit is overridden
		with a different unit.

``gavo_to_jd(d TIMESTAMP) -> DOUBLE PRECISION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function converts a postgres timestamp to julian date.
This is naive; no corrections for timezones, let alone time
scales or the like are done; you can thus not expect this to be
good to second-precision unless you are careful in the construction
of the timestamp.

``gavo_to_jd(d TIMESTAMP) -> REAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts a timestamp to a Julian date.
						Parameters:
							d: The SQL timestamp to convert.

``gavo_to_mjd(d TIMESTAMP) -> DOUBLE PRECISION``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function converts a postgres timestamp to modified julian date.
This is naive; no corrections for timezones, let alone time
scales or the like are done; you can thus not expect this to be
good to second-precision unless you are careful in the construction
of the timestamp.

``gavo_to_mjd(d TIMESTAMP) -> REAL``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Converts a timestamp to modified Julian date.
						Parameters:
							d: The SQL timestamp to convert.

``gavo_transform(from_sys TEXT, to_sys TEXT, geo GEOMETRY) -> GEOMETRY``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function transforms ADQL geometries between various reference systems.
geo can be a POINT, a CIRCLE, or a POLYGON, and the function will return a
geometry of the same type.  In the current implementation, from_sys and
to_sys must be literal strings (i.e., they cannot be computed through
expressions or be taken from database columns).

All transforms are just simple rotations, which is only a rough 
approximation to the actual relationships between reference systems
(in particular between FK4 and ICRS-based ones).  Note that, in particular,
the epoch is not changed (i.e., no proper motions are applied).

We currently support the following reference frames: ICRS, FK5 (which
is treated as ICRS), FK4 (for B1950. without epoch-dependent corrections),
GALACTIC.  Reference frame names are case-sensitive.

``gavo_transform(from_sys VARCHAR, to_sys VARCHAR, geo VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function transforms ADQL geometries between various reference systems.
						Parameters:
							from_sys: name of the source reference system.
							to_sys: name of the target reference system.
							geo: an ADQL geometry (POINT, CIRCLE, POLYGON).

``gavo_transform(from_sys VARCHAR, to_sys VARCHAR, lower REAL, geo VARCHAR, upper REAL, nbins INTEGER) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function transforms ADQL geometries between various reference systems.
						Parameters:
							from_sys: name of the source reference system.
							to_sys: name of the target reference system.
							lower: the lower limit of the histogram
							geo: an ADQL geometry (POINT, CIRCLE, POLYGON).
							upper: the upper limit of the histogram
							nbins: the number of "natural" bins in the histogram.

``gavo_vocmatch(vocname TEXT, term TEXT, matchagainst TEXT) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
returns 1 if matchagainst is term or narrower in the IVOA vocabulary
vocname, 0 otherwise.

This is intended for semantic querying.  For instance, 
gavo_vocmatch('datalink/core', 'calibration', semantics) would be 1
if semantics is any of calibration, bias, dark, or flat.

For RDF-flavoured vocabularies (strict trees), term will expand to the
entire branch rooted in term.  For SKOS-flavoured vocabularies (where
narrower is not transitive), only directly narrower terms will be included.

Both the term and the vocabulary name must be string literals (i.e.,
constants).  matchagainst can be any string-valued expression.

``greatest(v1 DOUBLE, v2 DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the greatest value between the two

``healpix(ra DOUBLE, dec DOUBLE) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
position to HEALPix in the indexed database order (obsolete)

``healpix(ra DOUBLE, dec DOUBLE, order INTEGER) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
position to HEALPix in the indexed database order (obsolete)

``initcap(txt VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``least(v1 DOUBLE, v2 DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the lowest value between the two

``log(b DOUBLE, x DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Logarithm to base b
						Parameters:
							b: null
							x: null

``lowercase(str VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Put all characters of the given string in lower-case.

``normId(id VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Normalise the given Simbad's object identifier (e.g. 'm1', 'andromeda').

``radec2sexa(ra DOUBLE, dec DOUBLE, prec SMALLINT) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Format the given coordinates into a Sexagesimal notation.

``radial_velocity(parallax DOUBLE, pm_rv DOUBLE) ->``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the radial velocity in units of mas/yr
						Parameters:
							parallax: Parallax (mas)
							pm_rv: Radial proper motion (mas/yr)

``random() -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^

``regexp(str VARCHAR, pattern VARCHAR) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Determine whether the given string - str - matches the given regular expression - pattern. If yes, 1 is returned, else 0.

``rpad(txt VARCHAR, len INTEGER, fill VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``rtrim(txt VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``sign(x DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sign of the argument (-1, 0, +1)
						Parameters:
							x: null

``smb_get_ids(oid BIGINT, maximum DOUBLE) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Aggregate inside a single string the identifiers of the given oid. Row value are separated by pipe string (limited to maximum given).

``stddev(n DOUBLE) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Standard deviation
						Parameters:
							n: null

``string_agg(str VARCHAR, delim VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Aggregate inside a single string the value of the given expression for each row. Row value are separated by the given string - delim.

``to_char(v1,v2)() -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Convert valid values into char data type, following the format defined in v2
						Parameters:

``unnest(column DOUBLE[]) -> DOUBLE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns an array column in a per-row basis. When it is used for multiple columns, each row will contain a[0], b[0], but be aware that lengths my differ.

``uppercase(str VARCHAR) -> VARCHAR``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Put all characters of the given string in upper-case.

``width_bucket(operand DOUBLE, min DOUBLE, max DOUBLE, buckets DOUBLE) -> INTEGER``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Returns the bucket number to which operand would be assigned in a histogram having count equal-width buckets spanning the range min to max; returns 0 or count+1 for an input outside the range
						Parameters:
							operand: null
							min: null
							max: null
							buckets: null

